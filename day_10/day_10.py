import time

from copy import deepcopy
from typing import List


OPEN_CLOSE = {"(": ")", "[": "]", "{": "}", "<": ">"}
PART_1_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
PART_2_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def part_1(input: List[List[str]]) -> int:

    score = 0
    for line in input:
        stack = []
        for char in line:
            if char in ["(", "[", "{", "<"]:
                stack.insert(0, OPEN_CLOSE[char])
                continue

            if stack[0] != char:
                score += PART_1_SCORES[char]
                break

            stack.pop(0)

    return score


def part_2(input: List[List[str]]) -> int:
    to_remove = []
    scores = []

    for i, line in enumerate(input):
        stack = []
        for char in line:
            if char in ["(", "[", "{", "<"]:
                stack.insert(0, OPEN_CLOSE[char])
                continue

            if stack[0] != char:
                to_remove.append(i)
                break

            stack.pop(0)

    for i in to_remove[::-1]:
        input.pop(i)

    for i, line in enumerate(input):
        stack = []
        for char in line:
            if char in ["(", "[", "{", "<"]:
                stack.insert(0, OPEN_CLOSE[char])
                continue

            stack.pop(0)

        score = 0
        for char in stack:
            score *= 5
            score += PART_2_SCORES[char]
        scores.append(score)

    mid = int((len(scores) - 1) / 2)
    return (sorted(scores))[mid]


if __name__ == "__main__":
    f = open("day_10.txt", "r")
    input = f.read().splitlines()

    start_1 = time.time()
    res_1 = part_1(deepcopy(input))
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(deepcopy(input))
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
