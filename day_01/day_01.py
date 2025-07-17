#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from day import Day


class Day1(Day):
    def __init__(self) -> None:
        super().__init__(1)

    def parse_data(self) -> np.ndarray:
        elves = [0]
        for row in self.raw_data:
            if row.strip() == "":
                elves.append(0)
            else:
                elves[-1] += int(row.strip())
        return np.array(elves)

    def part_1(self) -> int:
        return np.max(self.data)

    @property
    def part_1_solution(self) -> int:
        return 70369

    def part_2(self) -> int:
        self.data.sort()
        return self.data[-3:].sum()

    @property
    def part_2_solution(self) -> int:
        return 203002
