import time

from copy import deepcopy
from typing import List


def part_1() -> int:
    return -1


def part_2() -> int:
    return -1


if __name__ == "__main__":
    f = open("day_12.txt", "r")
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
