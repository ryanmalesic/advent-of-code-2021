import time

from typing import List, Tuple


def find_valid_dx(x_range: Tuple[int, int]) -> List[int]:
    min_dx = 0

    while sum(range(min_dx + 1)) < x_range[0]:
        min_dx += 1

    valid_dx = set()

    for dx in range(min_dx, x_range[1] + 1):
        for i in range(dx + 1):
            x = sum(range(i, dx + 1))
            if x >= x_range[0] and x <= x_range[1]:
                valid_dx.add(dx)

    return list(valid_dx)


def test_velocity(
    velocity: List[int], x_range: Tuple[int, int], y_range: Tuple[int, int]
) -> bool:
    pos = [0, 0]
    while True:
        if pos[0] in list(range(x_range[0], x_range[1] + 1)) and pos[1] in list(
            range(y_range[0], y_range[1] + 1)
        ):
            return True

        if pos[0] > x_range[1] or pos[1] < y_range[0]:
            return False

        pos[0] += velocity[0]
        pos[1] += velocity[1]
        velocity[0] -= 1 if velocity[0] > 0 else 0
        velocity[1] -= 1


def find_initial_velocities(
    x_range: Tuple[int, int], y_range: Tuple[int, int]
) -> List[Tuple[int, int]]:
    initial_velocities = []

    valid_dx = find_valid_dx(x_range)
    valid_dy = list(range(y_range[0], -(y_range[0] + 1) + 1))

    for dx in valid_dx:
        for dy in valid_dy:
            if test_velocity([dx, dy], x_range, y_range):
                initial_velocities.append((dx, dy))

    return initial_velocities


def part_1(min_y: int) -> int:
    # min_dx = find_min_dx(x_range)
    max_dy = -(min_y + 1)
    return sum(range(max_dy + 1))


def part_2(x_range: Tuple[int, int], y_range: Tuple[int, int]) -> int:
    inital_velocities = find_initial_velocities(x_range, y_range)

    return len(inital_velocities)


if __name__ == "__main__":
    f = open("day_17.txt", "r")
    input = f.read().splitlines()[0]

    first_equals = input.find("=")
    second_equals = input.find("=", first_equals + 1)
    comma = input.find(",")

    x_min, x_max = input[first_equals + 1 : comma].split("..")
    y_min, y_max = input[second_equals + 1 :].split("..")

    x_range = (int(x_min), int(x_max))
    y_range = (int(y_min), int(y_max))

    start_1 = time.time()
    res_1 = part_1(int(y_min))
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(x_range, y_range)
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")


oof = [
    (6, 0),
    (6, 1),
    (7, -1),
    (7, 0),
    (8, -2),
    (8, -1),
    (9, -2),
    (9, -1),
    (10, -2),
    (10, -1),
    (11, -4),
    (11, -3),
    (11, -2),
    (12, -4),
    (12, -3),
    (12, -2),
    (13, -4),
    (13, -3),
    (13, -2),
    (14, -4),
    (14, -3),
    (14, -2),
    (15, -4),
    (15, -3),
    (15, -2),
    (20, -10),
    (20, -9),
    (20, -8),
    (20, -7),
    (20, -6),
    (20, -5),
    (21, -10),
    (21, -9),
    (21, -8),
    (21, -7),
    (21, -6),
    (21, -5),
    (22, -10),
    (22, -9),
    (22, -8),
    (22, -7),
    (22, -6),
    (22, -5),
    (23, -10),
    (23, -9),
    (23, -8),
    (23, -7),
    (23, -6),
    (23, -5),
    (24, -10),
    (24, -9),
    (24, -8),
    (24, -7),
    (24, -6),
    (24, -5),
    (25, -10),
    (25, -9),
    (25, -8),
    (25, -7),
    (25, -6),
    (25, -5),
    (26, -10),
    (26, -9),
    (26, -8),
    (26, -7),
    (26, -6),
    (26, -5),
    (27, -10),
    (27, -9),
    (27, -8),
    (27, -7),
    (27, -6),
    (27, -5),
    (28, -10),
    (28, -9),
    (28, -8),
    (28, -7),
    (28, -6),
    (28, -5),
    (29, -10),
    (29, -9),
    (29, -8),
    (29, -7),
    (29, -6),
    (29, -5),
    (30, -10),
    (30, -9),
    (30, -8),
    (30, -7),
    (30, -6),
    (30, -5),
]
