import time

from typing import List, Tuple


def part_1(to_from: List[List[Tuple[int, int]]]) -> int:
    filtered = [x for x in to_from if x[0][0] == x[1][0] or x[0][1] == x[1][1]]

    max_x = -1
    max_y = -1
    for pairs in filtered:
        for pair in pairs:
            max_x = pair[0] if pair[0] > max_x else max_x
            max_y = pair[1] if pair[1] > max_y else max_y

    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for pairs in filtered:
        x1 = pairs[0][0]
        y1 = pairs[0][1]
        x2 = pairs[1][0]
        y2 = pairs[1][1]

        if x1 == x2:
            if y2 > y1:
                for y in range(y1, y2 + 1):
                    grid[y][x1] += 1
            else:
                for y in range(y2, y1 + 1):
                    grid[y][x1] += 1

        if y1 == y2:
            if x2 > x1:
                for x in range(x1, x2 + 1):
                    grid[y1][x] += 1
            else:
                for x in range(x2, x1 + 1):
                    grid[y1][x] += 1

    sum = 0
    for row in grid:
        for num in row:
            if num > 1:
                sum += 1
    return sum


def part_2(to_from: List[List[Tuple[int, int]]]) -> int:
    max_x = -1
    max_y = -1
    for pairs in to_from:
        for pair in pairs:
            max_x = pair[0] if pair[0] > max_x else max_x
            max_y = pair[1] if pair[1] > max_y else max_y

    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for pairs in to_from:
        x1 = pairs[0][0]
        y1 = pairs[0][1]
        x2 = pairs[1][0]
        y2 = pairs[1][1]

        if x1 == x2:
            if y2 > y1:
                for y in range(y1, y2 + 1):
                    grid[y][x1] += 1
            else:
                for y in range(y2, y1 + 1):
                    grid[y][x1] += 1

        elif y1 == y2:
            if x2 > x1:
                for x in range(x1, x2 + 1):
                    grid[y1][x] += 1
            else:
                for x in range(x2, x1 + 1):
                    grid[y1][x] += 1

        else:
            diff_x = x2 - x1
            diff_y = y2 - y1

            points = []
            for x in range(x1, x1 + diff_x, int(diff_x / abs(diff_x))):
                points.append([x, 0])

            for i, y in enumerate(range(y1, y1 + diff_y, int(diff_y / abs(diff_y)))):
                points[i][1] = y

            points.append([x2, y2])

            for point in points:
                grid[point[1]][point[0]] += 1

    sum = 0
    for row in grid:
        for num in row:
            if num > 1:
                sum += 1
    return sum


if __name__ == "__main__":
    f = open("day_5.txt", "r")
    input = list(map(lambda x: x.strip(), f.readlines()))

    to_from = [
        [(int(y.split(",")[0]), int(y.split(",")[1])) for y in x.split(" -> ")]
        for x in input
    ]

    start_1 = time.time()
    res_1 = part_1(to_from)
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(to_from)
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
