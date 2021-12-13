import time

from copy import deepcopy
from typing import List


def flash(grid: List[List[int]], flashed: List[List[bool]], m: int, n: int):
    if grid[m][n] < 10 or flashed[m][n]:
        return

    flashed[m][n] = True

    for dm in [-1, 0, 1]:
        for dn in [-1, 0, 1]:
            if dm == 0 and dn == 0:
                continue

            if m + dm < 0 or m + dm >= len(grid):
                continue

            if n + dn < 0 or n + dn >= len(grid[0]):
                continue

            grid[m + dm][n + dn] += 1
            flash(grid, flashed, m + dm, n + dn)


def part_1(input: List[List[int]]) -> int:
    flashes = 0

    for step in range(100):
        for m, row in enumerate(input):
            for n, octopus in enumerate(row):
                input[m][n] += 1

        flashed = [[False for _ in m] for m in input]

        for m, row in enumerate(input):
            for n, octopus in enumerate(row):
                flash(input, flashed, m, n)

        for m, row in enumerate(flashed):
            for n, f in enumerate(row):
                if f:
                    flashes += 1
                    input[m][n] = 0

    return flashes


def part_2(input: List[List[int]]) -> int:
    step = 1
    while True:

        for m, row in enumerate(input):
            for n, octopus in enumerate(row):
                input[m][n] += 1

        flashed = [[False for _ in m] for m in input]

        for m, row in enumerate(input):
            for n, octopus in enumerate(row):
                flash(input, flashed, m, n)

        all_flashed = True

        for row in flashed:
            if not all(row):
                all_flashed = False

        if all_flashed:
            return step

        for m, row in enumerate(flashed):
            for n, f in enumerate(row):
                if f:
                    input[m][n] = 0
        step += 1


if __name__ == "__main__":
    f = open("day_11.txt", "r")
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
