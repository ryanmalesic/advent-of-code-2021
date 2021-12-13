import time

from collections import Counter
from typing import List


def part_1(input: List[str]) -> int:
    width = len(input[0])
    gamma = ""
    epsilon = ""

    for i in range(width):
        counter = Counter([line[i] for line in input])
        gamma += "0" if counter["0"] > counter["1"] else "1"
        epsilon += "0" if counter["0"] < counter["1"] else "1"

    return int(gamma, 2) * int(epsilon, 2)


def part_2(input: List[str]) -> int:
    width = len(input[0])
    copy_oxy = input.copy()
    copy_co2 = input.copy()

    for i in range(width):
        counter_oxy = Counter([line[i] for line in copy_oxy])
        counter_co2 = Counter([line[i] for line in copy_co2])

        most_common = "0" if counter_oxy["0"] > counter_oxy["1"] else "1"
        least_common = "0" if counter_co2["0"] <= counter_co2["1"] else "1"

        if len(copy_oxy) > 1:
            copy_oxy = [x for x in copy_oxy if x[i] == most_common]
        if len(copy_co2) > 1:
            copy_co2 = [x for x in copy_co2 if x[i] == least_common]

        if len(copy_oxy) == 1 and len(copy_co2) == 1:
            break

    oxy = copy_oxy[0]
    co2 = copy_co2[0]

    return int(oxy, 2) * int(co2, 2)


if __name__ == "__main__":
    f = open("day_3.txt", "r")
    input = list(map(lambda x: x.strip(), f.readlines()))

    start_1 = time.time()
    res_1 = part_1(input)
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(input)
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
