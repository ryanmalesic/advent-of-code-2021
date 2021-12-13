import time

from copy import deepcopy
from typing import List, Tuple


def part_1(grid: List[List[bool]], folds: List[Tuple[str, int]]) -> int:
    fold = folds[0]

    if fold[0] == "x":
        for m in range(0, len(grid)):
            for dn in range(1, len(grid[m]) - fold[1]):
                grid[m][fold[1] - dn] = grid[m][fold[1] - dn] or grid[m][fold[1] + dn]

        for m, row in enumerate(grid):
            grid[m] = row[0 : fold[1]]

    else:
        for dm in range(1, len(grid) - fold[1]):
            for n in range(0, len(grid[0])):
                grid[fold[1] - dm][n] = grid[fold[1] - dm][n] or grid[fold[1] + dm][n]

        grid = grid[0 : fold[1]]

    dots = 0

    for row in grid:
        for dot in row:
            dots += 1 if dot else 0

    return dots


def part_2(grid: List[List[bool]], folds: List[Tuple[str, int]]) -> int:
    for fold in folds:
        if fold[0] == "x":
            for m in range(0, len(grid)):
                for dn in range(1, len(grid[m]) - fold[1]):
                    grid[m][fold[1] - dn] = (
                        grid[m][fold[1] - dn] or grid[m][fold[1] + dn]
                    )

            for m, row in enumerate(grid):
                grid[m] = row[0 : fold[1]]

        else:
            for dm in range(1, len(grid) - fold[1]):
                for n in range(0, len(grid[0])):
                    grid[fold[1] - dm][n] = (
                        grid[fold[1] - dm][n] or grid[fold[1] + dm][n]
                    )

            grid = grid[0 : fold[1]]

    for row in grid:
        string = ""
        for dot in row:
            string += "#" if dot else "."
        print(string)

    return -1


def parse_input(input: List[str]) -> Tuple[List[List[bool]], List[Tuple[str, int]]]:
    folds = []

    coords = []
    max_x = 0
    max_y = 0
    for line in input:
        if line == "":
            continue
        elif line.startswith("fold"):
            folds.append((line[11], int(line[13:])))
        else:
            x = int(line.split(",")[0])
            y = int(line.split(",")[1])

            max_x = max(max_x, x)
            max_y = max(max_y, y)

            coords.append((x, y))

    grid = [[False for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for coord in coords:
        grid[coord[1]][coord[0]] = True

    return (grid, folds)


if __name__ == "__main__":
    f = open("day_13.txt", "r")
    input = f.read().splitlines()

    grid, folds = parse_input(input)

    start_1 = time.time()
    res_1 = part_1(deepcopy(grid), deepcopy(folds))
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(deepcopy(grid), deepcopy(folds))
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
