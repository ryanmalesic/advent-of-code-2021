import time

from collections import defaultdict
from copy import deepcopy
from typing import Dict, List


def traverse(
    cave_system: Dict[str, List[str]],
    current: str,
    visited: List[str],
    path: List[str],
    paths: List[List[str]],
):
    if current == "end":
        paths.append(path)
        return

    for neighbor in cave_system[current]:
        if neighbor in visited:
            continue

        new_visited = visited.copy()
        if neighbor.islower():
            new_visited += [neighbor]

        traverse(cave_system, neighbor, new_visited, path + [neighbor], paths)


def traverse_2(
    cave_system: Dict[str, List[str]],
    current: str,
    visited: List[str],
    path: List[str],
    paths: List[List[str]],
    small_visited_twice: bool,
):

    if current == "end":
        paths.append(path)
        return

    for neighbor in cave_system[current]:
        if neighbor.islower():
            if neighbor in visited and small_visited_twice:
                continue

            if (
                neighbor in visited
                and not small_visited_twice
                and neighbor != "start"
                and neighbor != "end"
            ):

                traverse_2(
                    cave_system, neighbor, visited, path + [neighbor], paths, True
                )

            if neighbor not in visited:
                traverse_2(
                    cave_system,
                    neighbor,
                    visited + [neighbor],
                    path + [neighbor],
                    paths,
                    small_visited_twice,
                )

        else:
            traverse_2(
                cave_system,
                neighbor,
                visited,
                path + [neighbor],
                paths,
                small_visited_twice,
            )


def part_1(cave_system: Dict[str, List[str]]) -> int:
    paths = []
    traverse(cave_system, "start", ["start"], ["start"], paths)

    return len(paths)


def part_2(cave_system: Dict[str, List[str]]) -> int:
    paths = []
    traverse_2(cave_system, "start", ["start"], ["start"], paths, False)

    return len(paths)


def parse_input(input: List[str]) -> Dict[str, List[str]]:
    cave_system = defaultdict(list)

    for line in input:
        f, t = line.split("-")
        cave_system[f] += [t]
        cave_system[t] += [f]

    return dict(cave_system)


if __name__ == "__main__":
    f = open("day_12.txt", "r")
    input = f.read().splitlines()

    cave_system = parse_input(input)

    start_1 = time.time()
    res_1 = part_1(deepcopy(cave_system))
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(deepcopy(cave_system))
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
