import time

from typing import List


def check_board(board: List[List[int]]) -> bool:
    for row in board:
        if all(map(lambda x: x == -1, row)):
            return True

    cols = [[board[row][c] for row in range(5)] for c in range(5)]

    for col in cols:
        if all(map(lambda x: x == -1, col)):
            return True

    return False


def calculate_answer(number: int, board: List[List[int]]) -> int:
    sum = 0
    for row in board:
        for num in row:
            sum += 0 if num == -1 else num

    return sum * number


def part_1(numbers: List[int], boards: List[List[List[int]]]) -> int:
    for number in numbers:
        for b, board in enumerate(boards):
            for m, row in enumerate(board):
                for n, board_num in enumerate(row):
                    if board_num == number:
                        boards[b][m][n] = -1

            is_winner = check_board(board)
            if is_winner:
                return calculate_answer(number, board)


def part_2(numbers: List[int], boards: List[List[List[int]]]) -> int:
    for number in numbers:
        winners = []

        for b, board in enumerate(boards):
            for m, row in enumerate(board):
                for n, board_num in enumerate(row):
                    if board_num == number:
                        boards[b][m][n] = -1

            is_winner = check_board(board)
            if is_winner:
                winners.append(b)

        if len(boards) == 1 and len(winners) == 1:
            return calculate_answer(number, board)

        for b in winners[::-1]:
            boards.pop(b)


if __name__ == "__main__":
    f = open("day_4.txt", "r")
    input = list(map(lambda x: x.strip(), f.readlines()))

    numbers = [int(x) for x in input[0].split(",")]
    boards = [
        [[int(z) for z in y.split()] for y in input[x : x + 5]]
        for x in range(2, len(input), 6)
    ]

    start_1 = time.time()
    res_1 = part_1(numbers, boards)
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(numbers, boards)
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
