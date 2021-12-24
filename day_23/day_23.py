import heapq as hq
import time


from functools import cache
from itertools import product

WEIGHTS = {"A": 1, "B": 10, "C": 100, "D": 1000}
INVALID_HALLS = (2, 4, 6, 8)
HALLS = tuple(range(0, 11))
ROOMS = tuple(range(11, 27))
NEIGHBORS = {
    0: (1,),
    1: (0, 2),
    2: (1, 3, 11),
    3: (2, 4),
    4: (3, 5, 12),
    5: (4, 6),
    6: (5, 7, 13),
    7: (6, 8),
    8: (7, 9, 14),
    9: (8, 10),
    10: (9,),
    11: (2, 15),
    12: (4, 16),
    13: (6, 17),
    14: (8, 18),
    15: (11, 19),
    16: (12, 20),
    17: (13, 21),
    18: (14, 22),
    19: (15, 23),
    20: (16, 24),
    21: (17, 25),
    22: (18, 26),
    23: (19,),
    24: (20,),
    25: (21,),
    26: (22,),
}
AROOMS = [11, 15, 19, 23]
BROOMS = [12, 16, 20, 24]
CROOMS = [13, 17, 21, 25]
DROOMS = [14, 18, 22, 26]

MODULO_ROOM = {0: "A", 1: "B", 2: "C", 3: "D"}

State = tuple[str]


def parse_state(lines: list[str]) -> State:
    return create_state(
        [
            (0, "" if lines[1][1] == "." else lines[1][1]),
            (1, "" if lines[1][2] == "." else lines[1][2]),
            (2, "" if lines[1][3] == "." else lines[1][3]),
            (3, "" if lines[1][4] == "." else lines[1][4]),
            (4, "" if lines[1][5] == "." else lines[1][5]),
            (5, "" if lines[1][6] == "." else lines[1][6]),
            (6, "" if lines[1][7] == "." else lines[1][7]),
            (7, "" if lines[1][8] == "." else lines[1][8]),
            (8, "" if lines[1][9] == "." else lines[1][9]),
            (9, "" if lines[1][10] == "." else lines[1][10]),
            (10, "" if lines[1][11] == "." else lines[1][11]),
            (11, "" if lines[2][3] == "." else lines[2][3]),
            (12, "" if lines[2][5] == "." else lines[2][5]),
            (13, "" if lines[2][7] == "." else lines[2][7]),
            (14, "" if lines[2][9] == "." else lines[2][9]),
            (15, "" if lines[3][3] == "." else lines[3][3]),
            (16, "" if lines[3][5] == "." else lines[3][5]),
            (17, "" if lines[3][7] == "." else lines[3][7]),
            (18, "" if lines[3][9] == "." else lines[3][9]),
            (19, "" if lines[4][3] == "." else lines[4][3]),
            (20, "" if lines[4][5] == "." else lines[4][5]),
            (21, "" if lines[4][7] == "." else lines[4][7]),
            (22, "" if lines[4][9] == "." else lines[4][9]),
            (23, "" if lines[5][3] == "." else lines[5][3]),
            (24, "" if lines[5][5] == "." else lines[5][5]),
            (25, "" if lines[5][7] == "." else lines[5][7]),
            (26, "" if lines[5][9] == "." else lines[5][9]),
        ]
    )


def create_state(amphipods: list[tuple[int, str]]) -> State:
    halls = ["" for _ in range(11)]
    rooms = ["" for _ in range(4) for r in range(4)]
    cells = halls + rooms

    for a in amphipods:
        cells[a[0]] = a[1]

    return tuple(cells)


def done(state: State) -> bool:
    return state[11:] == (
        "A",
        "B",
        "C",
        "D",
        "A",
        "B",
        "C",
        "D",
        "A",
        "B",
        "C",
        "D",
        "A",
        "B",
        "C",
        "D",
    )


@cache
def cost(state: State, s: int, d: int):
    q = [(0, s)]
    seen = set()

    while q:
        cost, i = hq.heappop(q)

        if i == d:
            return cost

        for n in NEIGHBORS[i]:
            if n in seen:
                continue

            hq.heappush(q, (1 + cost if state[n] == "" else float("inf"), n))
            seen.add(n)


@cache
def moves(state: State) -> tuple[tuple[int, int]]:
    m = []

    for s, d in product(range(27), repeat=2):
        if s == d:
            continue
        if state[s] == "":
            continue
        if state[d] != "":
            continue
        if s in HALLS and d in HALLS:
            continue

        if s in AROOMS and d in AROOMS:
            continue
        if s in BROOMS and d in BROOMS:
            continue
        if s in CROOMS and d in CROOMS:
            continue
        if s in DROOMS and d in DROOMS:
            continue

        if d in INVALID_HALLS:
            continue

        if cost(state, s, d) == float("inf"):
            continue

        if d in ROOMS:
            if state[s] == "A" and d not in AROOMS:
                continue
            if state[s] == "B" and d not in BROOMS:
                continue
            if state[s] == "C" and d not in CROOMS:
                continue
            if state[s] == "D" and d not in DROOMS:
                continue

            layer = int((d - 11) / 4) + 1
            start = ((d - 11) % 4) + 11 + (4 * (layer))

            if d in AROOMS and any(map(lambda i: state[i] != "A", range(start, 27, 4))):
                continue
            if d in BROOMS and any(map(lambda i: state[i] != "B", range(start, 27, 4))):
                continue
            if d in CROOMS and any(map(lambda i: state[i] != "C", range(start, 27, 4))):
                continue
            if d in DROOMS and any(map(lambda i: state[i] != "D", range(start, 27, 4))):
                continue

        if s in ROOMS:
            if state[s] == "A" and s == AROOMS[-1]:
                continue
            if state[s] == "B" and s == BROOMS[-1]:
                continue
            if state[s] == "C" and s == CROOMS[-1]:
                continue
            if state[s] == "D" and s == DROOMS[-1]:
                continue

            layer = int((s - 11) / 4) + 1
            start = ((s - 11) % 4) + 11 + (4 * (layer))

            if (
                s in AROOMS
                and state[s] == "A"
                and all(map(lambda i: state[i] == "A", range(start, 27, 4)))
            ):
                continue
            if (
                s in BROOMS
                and state[s] == "B"
                and all(map(lambda i: state[i] == "B", range(start, 27, 4)))
            ):
                continue
            if (
                s in CROOMS
                and state[s] == "C"
                and all(map(lambda i: state[i] == "C", range(start, 27, 4)))
            ):
                continue
            if (
                s in DROOMS
                and state[s] == "D"
                and all(map(lambda i: state[i] == "D", range(start, 27, 4)))
            ):
                continue

        m.append((s, d))
    return tuple(m)


@cache
def go(state: State) -> int:
    if done(state):
        return 0

    min_cost = float("inf")

    for s, d in moves(state):
        c = cost(state, s, d) * WEIGHTS[state[s]]

        amphipods = [[i, v] for i, v in enumerate(state)]
        amphipods[s][1], amphipods[d][1] = "", amphipods[s][1]
        amphipods = [tuple(a) for a in amphipods]

        new_state = create_state(amphipods)

        min_cost = min(min_cost, c + go(new_state))

    return min_cost


def part_1() -> int:
    initial_state = create_state(
        [
            (11, "D"),
            (12, "D"),
            (13, "A"),
            (14, "A"),
            (15, "C"),
            (16, "C"),
            (17, "B"),
            (18, "B"),
            (19, "A"),
            (20, "B"),
            (21, "C"),
            (22, "D"),
            (23, "A"),
            (24, "B"),
            (25, "C"),
            (26, "D"),
        ]
    )

    return go(initial_state)


def part_2(input: list[str]) -> int:
    initial_state = parse_state(input)

    return go(initial_state)


if __name__ == "__main__":
    f = open("day_23.txt", "r")
    input = f.read().splitlines()

    print("Part\tResult\tTime")

    start_1 = time.time()
    res_1 = part_1()
    end_1 = time.time()
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")

    start_2 = time.time()
    res_2 = part_2(input)
    end_2 = time.time()
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
