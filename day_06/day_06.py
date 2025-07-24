#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day
from collections import deque


class Day6(Day):
    def __init__(self) -> None:
        super().__init__(6)

    def parse_data(self) -> str:
        return self.raw_data[0]

    def part_1(self) -> int:
        return self._find_distinct_characters(4)

    def _find_distinct_characters(self, buffer_size) -> int:
        read_buffer = deque(maxlen=buffer_size)
        for i, char in enumerate(self.data):
            read_buffer.append(char)
            if len(set(read_buffer)) == buffer_size:
                return i + 1  # 1-based index

        raise ValueError()

    @property
    def part_1_solution(self) -> int:
        return 1760

    def part_2(self) -> int:
        return self._find_distinct_characters(14)

    @property
    def part_2_solution(self) -> int:
        return 2974
