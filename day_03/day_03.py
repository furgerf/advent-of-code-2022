#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Iterable
from day import Day


class Day3(Day):
    def __init__(self) -> None:
        super().__init__(3)

    def parse_data(self) -> list[list[int]]:
        return [[Day3._parse_character(char) for char in row] for row in self.raw_data]

    @staticmethod
    def _parse_character(char: str) -> int:
        char_code = ord(char)
        return char_code - 38 if char_code < 96 else char_code - 96

    def part_1(self) -> int:
        priority = 0
        for rucksack in self.data:
            lower = set(rucksack[: len(rucksack) // 2])
            upper = set(rucksack[len(rucksack) // 2 :])
            priority += sum(lower.intersection(upper))
        return priority

    @property
    def part_1_solution(self) -> int:
        return 8240

    def part_2(self) -> int:
        priority = 0
        for a, b, c in Day3._batch_list(self.data, 3):
            priority += sum(set(a).intersection(b).intersection(c))
        return priority

    @staticmethod
    def _batch_list(full_list: list, batch_size: int) -> Iterable[list]:
        for i in range(0, len(full_list), batch_size):
            yield full_list[i : i + batch_size]

    @property
    def part_2_solution(self) -> int:
        return 2587
