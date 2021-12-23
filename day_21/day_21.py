import time

from functools import cache
from itertools import product


def ddice_roll_generator():
    roll = 0
    while True:
        roll += 1
        if roll == 101:
            roll = 1
        yield roll


def part_1(p1_pos: int, p2_pos: int) -> int:
    p1_score, p2_score = 0, 0
    dice_rolls = 0

    gen = ddice_roll_generator()

    while True:
        p1_moves = [next(gen), next(gen), next(gen)]
        p1_pos = (p1_pos + sum(p1_moves) - 1) % 10 + 1
        p1_score += p1_pos
        dice_rolls += 3
        if p1_score >= 1000:
            break

        p2_moves = [next(gen), next(gen), next(gen)]
        p2_pos = (p2_pos + sum(p2_moves) - 1) % 10 + 1
        p2_score += p2_pos
        dice_rolls += 3
        if p2_score >= 1000:
            break

    return min(p1_score, p2_score) * dice_rolls


@cache
def run(p1, s1, p2, s2, turn):
    if s1 >= 21:
        return 1, 0
    if s2 >= 21:
        return 0, 1

    ans = (0, 0)

    for rolls in product([1, 2, 3], repeat=3):
        new_p = ((p1 if turn == 1 else p2) + sum(rolls) - 1) % 10 + 1
        if turn == 1:
            w1, w2 = run(new_p, s1 + new_p, p2, s2, 2)
            ans = (ans[0] + w1, ans[1] + w2)
        else:
            w1, w2 = run(p1, s1, new_p, s2 + new_p, 1)
            ans = (ans[0] + w1, ans[1] + w2)

    return ans


def part_2(p1, p2):
    return max(run(p1, 0, p2, 0, 1))


if __name__ == "__main__":
    f = open("day_21.txt", "r")
    input = f.read().splitlines()

    p1 = int(input[0][-1])
    p2 = int(input[1][-1])

    start_1 = time.time()
    res_1 = part_1(p1, p2)
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(p1, p2)
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
