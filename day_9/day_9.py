import time

from copy import deepcopy
from typing import List


def is_lowest(
    heatmap: List[List[int]], m: int, n: int, row: List[int], val: int
) -> bool:
    for delta in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        new_m = m + delta[1]
        new_n = n + delta[0]

        if new_m >= 0 and new_m < len(heatmap) and new_n >= 0 and new_n < len(row):
            if heatmap[new_m][new_n] <= val:
                return False

    return True


def part_1(heatmap: List[List[int]]) -> int:
    lowest = []
    for m, row in enumerate(heatmap):
        for n, val in enumerate(row):
            if is_lowest(heatmap, m, n, row, val):
                lowest.append(val)

    return sum(lowest) + len(lowest)


def check_neighbors(heatmap: List[List[int]], m: int, n: int) -> int:
    if heatmap[m][n] == -1 or heatmap[m][n] == 9:
        return 0

    heatmap[m][n] = -1

    neighbors_sum = 1

    for delta in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        new_m = m + delta[1]
        new_n = n + delta[0]

        if (
            new_m >= 0
            and new_m < len(heatmap)
            and new_n >= 0
            and new_n < len(heatmap[m])
        ):
            neighbors_sum += check_neighbors(heatmap, new_m, new_n)

    return neighbors_sum


def part_2(heatmap: List[List[int]]) -> int:
    largest = []
    for m, row in enumerate(heatmap):
        for n, _ in enumerate(row):
            largest = sorted(largest + [check_neighbors(heatmap, m, n)], reverse=True)[
                :3
            ]

    return largest[0] * largest[1] * largest[2]


if __name__ == "__main__":
    f = open("day_9.txt", "r")
    input = [[int(y) for y in list(x)] for x in f.read().splitlines()]

    start_1 = time.time()
    res_1 = part_1(deepcopy(input))
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(deepcopy(input))
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
