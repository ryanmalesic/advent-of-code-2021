import re
import time

from math import prod
from typing import Counter

Cube = tuple[int, int, int, int, int, int]
Step = tuple[bool, Cube]
Steps = list[Step]


def intersects(c1: Cube, c2: Cube) -> bool:
    return all(c1[i] <= c2[i + 1] and c1[i + 1] >= c2[i] for i in range(0, 5, 2))


def intersection(c1: Cube, c2: Cube) -> Cube:
    return tuple((min if i & 1 else max)(c1[i], c2[i]) for i in range(6))


def volume(cube: Cube) -> int:
    return prod(cube[i + 1] - cube[i] + 1 for i in range(0, 5, 2))


def run(steps: Steps) -> int:
    cubes = Counter()

    for state, new_cube in steps:
        new_cubes = Counter()

        if state:
            new_cubes[new_cube] += 1

        for cube, count in cubes.items():
            if intersects(new_cube, cube):
                x = intersection(new_cube, cube)
                new_cubes[x] -= count

        cubes.update(new_cubes)

    return sum(volume(cube) * count for cube, count in cubes.items())


def part_1(steps: Steps) -> int:
    return run(
        list(
            filter(
                lambda step: all(
                    step[1][i] >= -50 and step[1][i + 1] <= 50 for i in range(0, 5, 2)
                ),
                steps,
            )
        )
    )


def part_2(steps: Steps) -> int:
    return run(steps)


def parse(input: list[str]) -> Steps:
    return [
        (line.startswith("on"), tuple(map(int, re.findall("-?[0-9]+", line))))
        for line in input
    ]


if __name__ == "__main__":
    f = open("day_22.txt", "r")
    input = f.read().splitlines()

    print("Part\tResult\tTime")

    start_1 = time.time()
    res_1 = part_1(parse(input))
    end_1 = time.time()
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")

    start_2 = time.time()
    res_2 = part_2(parse(input))
    end_2 = time.time()
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
