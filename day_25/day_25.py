import time

from collections import defaultdict
from copy import deepcopy

Map = tuple[tuple[str]]


def l2t(l: list[list]) -> tuple[tuple]:
    return tuple(map(tuple, l))


def t2l(t: tuple[tuple]) -> list[list]:
    return list(map(list, t))


def part_1(map: Map) -> int:
    h = len(map)
    w = len(map[0])

    seen = set()

    while map not in seen:
        seen.add(map)
        nmap = t2l(deepcopy(map))

        for y, row in enumerate(map):
            for x, _ in enumerate(row):
                if map[y][x] == ">" and map[y][(x + 1) % w] == ".":
                    nmap[y][(x + 1) % w] = ">"
                    nmap[y][x] = "."

        map = l2t(nmap)

        for y, row in enumerate(map):
            for x, _ in enumerate(row):
                if map[y][x] == "v" and map[(y + 1) % h][x] == ".":
                    nmap[(y + 1) % h][x] = "v"
                    nmap[y][x] = "."

        map = l2t(nmap)

    return len(seen)


def part_2(map: Map) -> int:
    return -1


if __name__ == "__main__":
    f = open("day_25.txt", "r")
    input = tuple(map(tuple, f.read().splitlines()))

    print("Part\tResult\tTime")

    start_1 = time.time()
    res_1 = part_1(deepcopy(input))
    end_1 = time.time()
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")

    start_2 = time.time()
    res_2 = part_2(deepcopy(input))
    end_2 = time.time()
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
