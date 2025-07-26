#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
import numpy as np

from day import Day


class Direction(Enum):
    L = "L"
    R = "R"
    U = "U"
    D = "D"


Instruction = tuple[Direction, int]


class Day9(Day):
    def __init__(self) -> None:
        super().__init__(9)

    def parse_data(self) -> list[Instruction]:
        return [Day9._parse_instruction(line) for line in self.raw_data]

    @staticmethod
    def _parse_instruction(line: str) -> Instruction:
        direction, count = line.split(" ")
        return Direction(direction), int(count)

    def part_1(self) -> int:
        head = tail = (0, 0)
        visited = {tail}
        for direction, count in self.data:
            for _ in range(count):
                # move head
                match direction:
                    case Direction.L:
                        head = (head[0], head[1] - 1)
                    case Direction.R:
                        head = (head[0], head[1] + 1)
                    case Direction.U:
                        head = (head[0] + 1, head[1])
                    case Direction.D:
                        head = (head[0] - 1, head[1])
                    case _:
                        assert False

                # move tail
                d_x = head[0] - tail[0]
                d_y = head[1] - tail[1]
                if abs(d_x) > 1 and abs(d_y) == 0:
                    # must (only) move x
                    tail = (tail[0] + np.sign(d_x), tail[1])
                elif abs(d_y) > 1 and abs(d_x) == 0:
                    # must (only) move y
                    tail = (tail[0], tail[1] + np.sign(d_y))
                elif abs(d_x) > 1 or abs(d_y) > 1:
                    # must move diagonally
                    assert np.sign(d_x)
                    assert np.sign(d_y)
                    tail = (tail[0] + np.sign(d_x), tail[1] + np.sign(d_y))

                visited.add(tail)

        return len(visited)

    @property
    def part_1_solution(self) -> int:
        return 6256

    def part_2(self) -> int:
        head = (0, 0)
        tails = [(0, 0) for _ in range(9)]
        visited = {tails[-1]}
        for direction, count in self.data:
            for _ in range(count):
                # move head
                match direction:
                    case Direction.L:
                        head = (head[0], head[1] - 1)
                    case Direction.R:
                        head = (head[0], head[1] + 1)
                    case Direction.U:
                        head = (head[0] + 1, head[1])
                    case Direction.D:
                        head = (head[0] - 1, head[1])
                    case _:
                        assert False

                # move tail
                previous = head
                for i, tail in enumerate(tails):
                    d_x = previous[0] - tail[0]
                    d_y = previous[1] - tail[1]
                    if abs(d_x) > 1 and abs(d_y) == 0:
                        # must (only) move x
                        tails[i] = (tail[0] + np.sign(d_x), tail[1])
                    elif abs(d_y) > 1 and abs(d_x) == 0:
                        # must (only) move y
                        tails[i] = (tail[0], tail[1] + np.sign(d_y))
                    elif abs(d_x) > 1 or abs(d_y) > 1:
                        # must move diagonally
                        assert np.sign(d_x)
                        assert np.sign(d_y)
                        tails[i] = (tail[0] + np.sign(d_x), tail[1] + np.sign(d_y))

                    previous = tail

                visited.add(tails[-1])

        return len(visited)

    @property
    def part_2_solution(self) -> int:
        return 2665
