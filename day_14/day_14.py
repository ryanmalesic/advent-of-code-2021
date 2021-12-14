from os import replace
import time

from collections import Counter, defaultdict
from copy import deepcopy
from math import ceil
from typing import Dict, List


def part_1(template: str, rules: Dict[str, str]) -> int:
    for _ in range(10):
        for i in range(len(template) - 2, -1, -1):
            left, right = template[i : i + 2]
            replacement = rules.get(left + right)
            template = template[: i + 1] + replacement + template[i + 1 :]

    counter = Counter(template)

    return counter.most_common()[0][1] - counter.most_common()[-1][1]


import itertools


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def part_2(template: str, rules: Dict[str, str]) -> int:
    pairs = list(pairwise(template))
    pairs_counter = dict(Counter(pairs))

    for _ in range(40):
        new_pairs_counter = defaultdict(int)

        for (left, right), times in pairs_counter.items():
            new_left_pair = (left, rules[left + right])
            new_right_pair = (rules[left + right], right)

            new_pairs_counter[new_left_pair] += times
            new_pairs_counter[new_right_pair] += times

        pairs_counter = new_pairs_counter

    letter_counter = defaultdict(int)
    for (left, right), value in pairs_counter.items():
        letter_counter[left] += value
        letter_counter[right] += value

    letter_counter = Counter(letter_counter)

    return ceil(letter_counter.most_common()[0][1] / 2) - ceil(
        letter_counter.most_common()[-1][1] / 2
    )


if __name__ == "__main__":
    f = open("day_14.txt", "r")
    input = f.read().splitlines()

    template = input[0]
    rules = {}
    for line in input[2:]:
        f, t = line.split(" -> ")
        rules[f] = t

    start_1 = time.time()
    res_1 = part_1(deepcopy(template), deepcopy(rules))
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(deepcopy(template), deepcopy(rules))
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
