import time
from collections import defaultdict


def image_to_pixels(image: list[str]) -> set[(int, int)]:
    pixels = set()

    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == "#":
                pixels.add((x, y))

    return pixels


def run_algorithm(
    algorithm: str, pixels: set[(int, int)], width: int, height: int, step: int = 0
) -> set[(int, int)]:
    new_pixels = set()

    min_x, max_x = 0 - step - 1, width + step
    min_y, max_y = 0 - step - 1, height + step

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            index_str = ""

            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    curr = (x + dx, y + dy)

                    if (curr[0] <= min_x or curr[0] >= max_x) and algorithm[0] == "#":
                        index_str += str(step % 2)
                        continue

                    if (curr[1] <= min_y or curr[1] >= max_y) and algorithm[0] == "#":
                        index_str += str(step % 2)
                        continue

                    index_str += "1" if curr in pixels else "0"

            index = int(index_str, base=2)
            if algorithm[index] == "#":
                new_pixels.add((x, y))

    return new_pixels


def part_1(algorithm: str, image: list[str]) -> int:
    height = len(image)
    width = len(image[0])

    pixels = image_to_pixels(image)

    for i in range(2):
        pixels = run_algorithm(algorithm, pixels, width, height, i)

    return len(pixels)


def part_2(algorithm: str, image: list[str]) -> int:
    height = len(image)
    width = len(image[0])

    pixels = image_to_pixels(image)

    for i in range(50):
        pixels = run_algorithm(algorithm, pixels, width, height, i)

    return len(pixels)


if __name__ == "__main__":
    f = open("day_20.txt", "r")
    input = f.read().splitlines()

    algorithm = input[0]
    image = input[2:]

    start_1 = time.time()
    res_1 = part_1(algorithm, image)
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(algorithm, image)
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
