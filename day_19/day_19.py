#################################################
#                                               #
# WARNING: THIS CODE IS BAD                     #
# EACH PART TAKES A LONG TIME TO RUN            #
# LIKE 5 MINUTES FOR EACH PART                  #
#                                               #
# PART 2'S ANSWER CAN BE FOUND IN PART 1        #
# BY CALLING MANHATTAN DISTANCE ON THE SCANNERS #
# BUT WHATEVER I DONT CARE                      #
#                                               #
#################################################

import operator
import time

from collections import defaultdict
from functools import reduce
from itertools import permutations
from math import prod
from typing import Dict, List, Tuple

ScannerCoords = List[Tuple[int, int, int]]
ScannerCoordsDict = Dict[int, ScannerCoords]


def rotations():
    rotations = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                rotations.append((x, y, z))
    return rotations


diff = lambda a: reduce(operator.sub, a)
abs_diff = lambda a: abs(reduce(operator.sub, a))


def sub_delta(c: Tuple[int, int, int], delta: Tuple[int, int, int]) -> ScannerCoords:
    return tuple(map(diff, zip(c, delta)))


def rotate(
    c: Tuple[int, int, int], rotation: Tuple[int, int, int]
) -> Tuple[int, int, int]:
    return tuple(map(prod, zip(c, rotation)))


def swap_xy(c: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return c[1], c[0], c[2]


def swap_xz(c: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return c[2], c[1], c[0]


def swap_yz(c: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return c[0], c[2], c[1]


def yzx(c: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return c[1], c[2], c[0]


def zxy(c: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return c[2], c[0], c[1]


def run(scsd: ScannerCoordsDict):
    scs0 = scsd[0]

    all_beacons = set(scs0)
    all_scanners = set()

    found = {key: False for key in scsd.keys()}
    found[0] = True

    while not all(list(found.values())):
        for scs1 in list(sorted(scsd.items(), key=lambda x: x[0]))[1:]:
            if scs1[0] == 0:
                continue

            if found[scs1[0]]:
                continue

            for i, sc0 in enumerate(all_beacons):
                for rotation in rotations():
                    for i in range(6):
                        rotated_scs1 = [rotate(sc1, rotation) for sc1 in scs1[1]]

                        if i == 0:
                            rotated_scs1 = rotated_scs1
                        if i == 1:
                            rotated_scs1 = [swap_xy(sc1) for sc1 in rotated_scs1]
                        if i == 2:
                            rotated_scs1 = [swap_xz(sc1) for sc1 in rotated_scs1]
                        if i == 3:
                            rotated_scs1 = [swap_yz(sc1) for sc1 in rotated_scs1]
                        if i == 4:
                            rotated_scs1 = [yzx(sc1) for sc1 in rotated_scs1]
                        if i == 5:
                            rotated_scs1 = [zxy(sc1) for sc1 in rotated_scs1]

                        for rotated_sc in rotated_scs1:
                            distance = tuple(map(diff, zip(sc0, rotated_sc)))
                            overlayed_scs1 = [
                                tuple(map(sum, zip(sc1, distance)))
                                for sc1 in rotated_scs1
                            ]

                            if len(set(overlayed_scs1) & set(all_beacons)) >= 12:
                                all_scanners.add(distance)
                                for s in overlayed_scs1:
                                    all_beacons.add(s)
                                print(scs1[0], len(all_beacons))
                                found[scs1[0]] = True

                                break

                        if found[scs1[0]]:
                            break
                    if found[scs1[0]]:
                        break
                if found[scs1[0]]:
                    break

    return all_beacons, all_scanners


def manhattan_distance(scanners: List[Tuple[int, int, int]]) -> int:
    max_distance = float("-inf")
    for s in permutations(scanners, 2):
        distance = sum(tuple(map(abs_diff, zip(s[0], s[1]))))
        max_distance = max(max_distance, distance)

    return max_distance


def part_1(scsd: ScannerCoordsDict) -> int:
    beacons, _ = run(scsd)
    return len(beacons)


def part_2(scsd: ScannerCoordsDict) -> int:
    _, scanners = run(scsd)
    return manhattan_distance(scanners)


if __name__ == "__main__":
    f = open("day_19.txt", "r")
    input = f.read().splitlines()

    scanner = -1
    scanner_coords = defaultdict(list)

    for line in input:
        if line == "":
            continue

        if line.startswith("--- "):
            scanner += 1
            continue

        coord = tuple(map(int, line.split(",")))
        scanner_coords[scanner].append(coord)

    start_1 = time.time()
    res_1 = part_1(dict(scanner_coords))
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(dict(scanner_coords))
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
