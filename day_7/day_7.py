import math
import time

from typing import List


def part_1(input: List[int]) -> int:
    min_pos = min(input)
    max_pos = max(input)

    min_distance = float("infinity")

    for alignment in range(min_pos, max_pos + 1):
        distance = 0
        for pos in input:
            distance += abs(pos - alignment)

        if distance < min_distance:
            min_distance = distance

    return min_distance


def part_2(input: List[int]) -> int:
    min_pos = min(input)
    max_pos = max(input)

    min_distance = float("infinity")

    for alignment in range(min_pos, max_pos + 1):
        distance = 0
        for pos in input:
            n = abs(pos - alignment)
            distance += (n * (n + 1)) / 2

        if distance < min_distance:
            min_distance = distance

    return min_distance


if __name__ == "__main__":
    f = open("day_7.txt", "r")
    input = [int(x) for x in f.readline().split(",")]

    start_1 = time.time()
    res_1 = part_1(input.copy())
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(input.copy())
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
