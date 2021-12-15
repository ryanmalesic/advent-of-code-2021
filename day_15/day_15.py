import heapq as hq
import time

from copy import deepcopy
from typing import Dict, List, Tuple


def dijkstras(grid: List[List[int]]) -> int:
    h, w = len(grid), len(grid[0])
    q = [(0, (0, 0))]
    seen = set()

    while q:
        risk, (x, y) = hq.heappop(q)

        if (x, y) == (w - 1, h - 1):
            return risk

        for x, y in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
            if x >= 0 and x < w and y >= 0 and y < h and (x, y) not in seen:
                hq.heappush(
                    q,
                    (risk + (h - y) + (w - x) + grid[y][x], (x, y)),
                )
                seen.add((x, y))


def inc_grid(grid: List[List[int]], inc: int):
    grid = deepcopy(grid)

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            grid[y][x] += inc

    return grid


def inc_row(row: List[int], inc: int):
    row = deepcopy(row)

    for i, _ in enumerate(row):
        row[i] += inc

    return row


def five_times_grid(grid: List[List[int]]):
    grid = (
        grid
        + inc_grid(grid, 1)
        + inc_grid(grid, 2)
        + inc_grid(grid, 3)
        + inc_grid(grid, 4)
    )
    grid = list(
        map(
            lambda row: row
            + inc_row(row, 1)
            + inc_row(row, 2)
            + inc_row(row, 3)
            + inc_row(row, 4),
            grid,
        )
    )

    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            grid[y][x] = grid[y][x] if grid[y][x] <= 9 else grid[y][x] - 9

    return grid


if __name__ == "__main__":
    f = open("day_15.txt", "r")
    input = f.read().splitlines()

    grid = [[int(y) for y in list(x)] for x in input]

    start_1 = time.time()
    res_1 = dijkstras(deepcopy(grid))
    end_1 = time.time()

    start_2 = time.time()
    res_2 = dijkstras(five_times_grid(grid))
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
