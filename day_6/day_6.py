import math
import time

from typing import List


def part_1(input: List[int]) -> int:
    for _ in range(80):
        new = 0
        for i, e in enumerate(input):
            if e == 0:
                input[i] = 6
                new += 1
            else:
                input[i] -= 1

        for _ in range(new):
            input.append(8)

    print(len(input))


def part_2(input: List[int]) -> int:
    latternfish = [0 for _ in range(9)]

    for x in input:
        latternfish[x] += 1

    for _ in range(256):
        latternfish_0 = latternfish[0]
        latternfish[0] = latternfish[1]
        latternfish[1] = latternfish[2]
        latternfish[2] = latternfish[3]
        latternfish[3] = latternfish[4]
        latternfish[4] = latternfish[5]
        latternfish[5] = latternfish[6]
        latternfish[6] = latternfish_0 + latternfish[7]
        latternfish[7] = latternfish[8]
        latternfish[8] = latternfish_0

    print(sum(latternfish))


if __name__ == "__main__":
    f = open("day_6.txt", "r")
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
