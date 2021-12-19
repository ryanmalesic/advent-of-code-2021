import time

from dataclasses import dataclass, field
from math import ceil, floor
from typing import List, Union
from uuid import UUID, uuid4


@dataclass
class Node:
    id: UUID = field(default_factory=uuid4)
    value: int = -1
    depth: int = 0

    def __repr__(self) -> str:
        return str(self.value)


RecList = List[Union["RecList", Node]]


def transform(l: RecList, depth=0):
    if isinstance(l[0], Node):
        l[0] = Node(value=l[0].value, depth=depth)
    if isinstance(l[1], Node):
        l[1] = Node(value=l[1].value, depth=depth)
    if isinstance(l[0], int):
        l[0] = Node(value=l[0], depth=depth)
    if isinstance(l[1], int):
        l[1] = Node(value=l[1], depth=depth)
    if isinstance(l[0], list):
        transform(l[0], depth + 1)
    if isinstance(l[1], list):
        transform(l[1], depth + 1)
    return l


def flatten(l: RecList) -> List[Node]:
    if isinstance(l, Node):
        return [l]
    return flatten(l[0]) + flatten(l[1])


def explode(l: RecList) -> RecList:
    flattened = flatten(l)
    stack = [(l[0], [0]), (l[1], [1])]

    while len(stack) > 0:
        curr_node, curr_path = stack.pop(0)

        if (
            isinstance(curr_node[0], Node)
            and isinstance(curr_node[1], Node)
            and curr_node[0].depth >= 4
        ):
            left_idx = flattened.index(curr_node[0])
            right_idx = flattened.index(curr_node[1])

            if left_idx > 0:
                flattened[left_idx - 1].value += curr_node[0].value

            if right_idx < len(flattened) - 1:
                flattened[right_idx + 1].value += curr_node[1].value

            indexed_curr = l[curr_path[0]]
            for index in curr_path[1:-1]:
                indexed_curr = indexed_curr[index]

            indexed_curr[curr_path[-1]] = Node(value=0, depth=curr_node[0].depth - 1)
            flattened = flatten(l)
            stack = [(l[0], [0]), (l[1], [1])]

        elif isinstance(curr_node[0], Node) and isinstance(curr_node[1], Node):
            pass
        elif isinstance(curr_node[0], Node):
            stack = [(curr_node[1], curr_path + [1])] + stack
        elif isinstance(curr_node[1], Node):
            stack = [(curr_node[0], curr_path + [0])] + stack
        else:
            stack = [
                (curr_node[0], curr_path + [0]),
                (curr_node[1], curr_path + [1]),
            ] + stack

    return l


def split(l: RecList) -> RecList:
    stack = [(l[0], [0]), (l[1], [1])]

    while len(stack) > 0:
        curr_node, curr_path = stack.pop(0)

        if isinstance(curr_node, Node):
            if curr_node.value > 9:
                old_depth = curr_node.depth

                indexed_curr = l[curr_path[0]]

                for index in curr_path[1:-1]:
                    indexed_curr = indexed_curr[index]

                indexed_curr[curr_path[-1]] = [
                    Node(value=int(floor(curr_node.value / 2)), depth=old_depth + 1),
                    Node(value=int(ceil(curr_node.value / 2)), depth=old_depth + 1),
                ]

                if old_depth == 3:
                    return l, True
                else:
                    stack = [(l[0], [0]), (l[1], [1])]
        else:
            stack = [
                (curr_node[0], curr_path + [0]),
                (curr_node[1], curr_path + [1]),
            ] + stack

    return l, False


def reduce(l: RecList) -> RecList:
    needs_explode = True

    while needs_explode:
        l = explode(l)
        l, needs_explode = split(l)

    return l


def magnitude(l: RecList) -> int:
    left, right = 0, 0
    if isinstance(l[0], list):
        left = magnitude(l[0])
    if isinstance(l[1], list):
        right = magnitude(l[1])
    if isinstance(l[0], Node):
        left = l[0].value
    if isinstance(l[1], Node):
        right = l[1].value

    return 3 * left + 2 * right


def part_1(input: List[str]) -> int:
    current = eval(input[0])
    for line in input[1:]:
        n = eval(line)
        snailfish_number = transform([current, n])
        reduced = reduce(snailfish_number)
        current = reduced

    return magnitude(current)


def part_2(input: List[str]) -> int:
    max_magnitude = float("-inf")

    for i, line_1 in enumerate(input):
        for j, line_2 in enumerate(input):
            if i == j:
                continue

            snailfish_number_x_y = magnitude(
                reduce(transform([eval(line_1), eval(line_2)]))
            )
            snailfish_number_y_x = magnitude(
                reduce(transform([eval(line_2), eval(line_1)]))
            )

            max_magnitude = max(
                max_magnitude, snailfish_number_x_y, snailfish_number_y_x
            )

    return max_magnitude


if __name__ == "__main__":
    f = open("day_18.txt", "r")
    input = f.read().splitlines()

    start_1 = time.time()
    res_1 = part_1(input)
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(input)
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
