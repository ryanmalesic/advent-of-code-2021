import time

from collections import Counter
from typing import List

NUM_WIRES = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}


def part_1(signal_patterns: List[str], output_values_list: List[str]) -> int:
    counter = Counter()

    for output_values in output_values_list:
        counter.update(output_values.split(" "))

    counts = {}
    for num in NUM_WIRES.keys():
        counts[num] = sum(
            map(
                lambda y: y[1],
                filter(lambda x: len(x[0]) == NUM_WIRES[num], counter.items()),
            )
        )

    return counts[1] + counts[4] + counts[7] + counts[8]


def part_2(signal_patterns: List[str], output_values_list: List[str]) -> int:
    output_sum = 0

    for i in range(len(signal_patterns)):
        number_string_map = {i: set() for i in range(10)}

        signal_pattern = [set(list(x)) for x in signal_patterns[i].split(" ")]
        output_values = [set(list(x)) for x in output_values_list[i].split(" ")]

        number_string_map[1] = [x for x in signal_pattern if len(x) == 2][0]
        number_string_map[4] = [x for x in signal_pattern if len(x) == 4][0]
        number_string_map[7] = [x for x in signal_pattern if len(x) == 3][0]
        number_string_map[8] = [x for x in signal_pattern if len(x) == 7][0]

        len_6 = [x for x in signal_pattern if len(x) == 6]

        for e in len_6:
            missing = (number_string_map[8] - e).pop()
            if missing in number_string_map[1]:
                number_string_map[6] = e

            if missing in number_string_map[4] and missing not in number_string_map[1]:
                number_string_map[0] = e

            if (
                missing not in number_string_map[4]
                and missing not in number_string_map[1]
            ):
                number_string_map[9] = e

        len_5 = [x for x in signal_pattern if len(x) == 5]

        for e in len_5:
            missing = number_string_map[8] - e
            if len(missing.intersection(number_string_map[1])) == 0:
                number_string_map[3] = e
                continue

            if len(missing.intersection(number_string_map[6])) == 1:
                number_string_map[5] = e
                continue

            number_string_map[2] = e

        output_str = ""
        for output_value in output_values:
            for num, string in number_string_map.items():
                if string == set(list(output_value)):
                    output_str += str(num)

        output_sum += int(output_str)

    return output_sum


if __name__ == "__main__":
    f = open("day_8.txt", "r")
    input = f.read().splitlines()

    signal_patterns = [x.split(" | ")[0] for x in input]
    output_values_list = [x.split(" | ")[1] for x in input]

    start_1 = time.time()
    res_1 = part_1(signal_patterns.copy(), output_values_list.copy())
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(signal_patterns.copy(), output_values_list.copy())
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
