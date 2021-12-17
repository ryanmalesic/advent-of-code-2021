import time

from dataclasses import dataclass, field
from math import prod
from typing import List, Tuple, Union


@dataclass
class Literal:
    version: int
    type_id: int
    value: int


@dataclass
class Operator:
    version: int
    type_id: int
    operands: List[Union[Literal, "Operator"]] = field(default_factory=list)


def greater_than(l: list):
    return 1 if l[0] > l[1] else 0


def less_than(l: list):
    return 1 if l[0] < l[1] else 0


def equal_to(l: list):
    return 1 if l[0] == l[1] else 0


FUNCTIONS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: greater_than,
    6: less_than,
    7: equal_to,
}


def parse_packet(binary: str) -> Tuple[Literal | Operator, str]:
    return parse_literal(binary) if binary[3:6] == "100" else parse_operator(binary)


def parse_literal(binary: str) -> Tuple[Literal, str]:
    version = int(binary[:3], base=2)
    type_id = int(binary[3:6], base=2)

    start = curr = 6
    end = 11

    while binary[curr] == "1":
        curr += 5
        end += 5

    value_binary = "".join(
        [c for i, c in enumerate(list(binary[start:end])) if i % 5 != 0]
    )
    value = int(value_binary, base=2)

    literal = Literal(version, type_id, value)

    return literal, binary[end:]


def parse_operator(binary: str) -> Tuple[Operator, str]:
    version = int(binary[:3], base=2)
    type_id = int(binary[3:6], base=2)

    operator = Operator(version, type_id)

    length_type_id = binary[6]
    if length_type_id == "0":
        length = int(binary[7:22], base=2)
        expected_remainder = binary[22 + length :]

        binary = binary[22:]
        while binary != expected_remainder:
            obj, remainder = parse_packet(binary)
            operator.operands.append(obj)
            binary = remainder

    else:
        num_packets = int(binary[7:18], base=2)
        binary = binary[18:]

        for _ in range(num_packets):
            obj, remainder = parse_packet(binary)
            operator.operands.append(obj)
            binary = remainder

    return operator, binary


def sum_versions(packet: Literal | Operator):
    if isinstance(packet, Literal):
        return packet.version

    return packet.version + sum(map(sum_versions, packet.operands))


def part_1(binary: str) -> int:
    top = parse_packet(binary)[0]
    return sum_versions(top)


def evaluate(packet: Literal | Operator):
    if isinstance(packet, Literal):
        return packet.value
    return FUNCTIONS[packet.type_id](list(map(evaluate, packet.operands)))


def part_2(binary: str) -> int:
    top = parse_packet(binary)[0]
    return evaluate(top)


if __name__ == "__main__":
    f = open("day_16.txt", "r")
    input = f.read().splitlines()

    binary = str(bin(int(input[0], base=16)))[2:]

    if len(binary) % 4 == 3:
        binary = "0" + binary

    if len(binary) % 4 == 2:
        binary = "00" + binary

    if len(binary) % 4 == 1:
        binary = "000" + binary

    if input[0].startswith("0"):
        binary = "0000" + binary

    start_1 = time.time()
    res_1 = part_1(binary)
    end_1 = time.time()

    start_2 = time.time()
    res_2 = part_2(binary)
    end_2 = time.time()

    print("Part\tResult\tTime")
    print(f"1\t{res_1}\t{(end_1 - start_1) * 1000}")
    print(f"2\t{res_2}\t{(end_2 - start_2) * 1000}")
