from typing import List, Tuple


def part_1(input: List[Tuple[str, int]]):
    pos, dep = 0, 0

    for ins in input:
        match ins:
            case ["forward", mag]:
                pos += mag
            case ["up", mag]:
                dep -= mag
            case ["down", mag]:
                dep += mag

    print(pos * dep)


def part_2(input: List[Tuple[str, int]]):
    pos, dep, aim = 0, 0, 0

    for ins in input:
        match ins:
            case ["forward", mag]:
                pos += mag
                dep += aim * mag
            case ["up", mag]:
                aim -= mag
            case ["down", mag]:
                aim += mag

    print(pos * dep)


if __name__ == "__main__":
    f = open("day_2.txt", "r")
    input = map(lambda x: x.split(), f.readlines())
    input = list(map(lambda x: (x[0], int(x[1])), input))

    part_1(input)
    part_2(input)
