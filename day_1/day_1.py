from typing import List


def part_1(input: List[int]):
    increased = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            increased += 1

    print(increased)


def part_2(input: List[int]):
    increased = 0
    for i in range(1, len(input) - 2):
        prev_sum = input[i - 1] + input[i] + input[i + 1]
        sum = input[i] + input[i + 1] + input[i + 2]

        if sum > prev_sum:
            increased += 1

    print(increased)


if __name__ == "__main__":
    f = open("day_1.txt", "r")
    input = list(map(lambda x: int(x), f.readlines()))

    part_1(input)
    part_2(input)
