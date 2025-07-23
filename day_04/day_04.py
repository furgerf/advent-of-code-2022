#!/usr/bin/env python
# -*- coding: utf-8 -*-


from day import Day

Section = tuple[int, int]


def parse_row(row: str) -> tuple[Section, Section]:
    first, second = row.split(",")
    return parse_section(first), parse_section(second)


def parse_section(section: str) -> Section:
    start, end = section.split("-")
    return int(start), int(end)


class Day4(Day):
    def __init__(self) -> None:
        super().__init__(4)

    def parse_data(self) -> list[tuple[Section, Section]]:
        return [parse_row(row) for row in self.raw_data]

    def part_1(self) -> int:
        contained = 0
        for first, second in self.data:
            if first[0] >= second[0] and first[1] <= second[1]:
                contained += 1
                continue

            if second[0] >= first[0] and second[1] <= first[1]:
                contained += 1

        return contained

    @property
    def part_1_solution(self) -> int:
        return 530

    def part_2(self) -> int:
        contained = 0
        for first, second in self.data:
            # [..xxxxxx.......]
            # [.....xxxxxxx...]
            if first[0] <= second[0] and first[1] >= second[0]:
                contained += 1
                continue

            # [.....xxxxxxx...]
            # [..xxxxxx.......]
            if first[0] <= second[1] and first[1] >= second[1]:
                contained += 1
                continue

            # [...xxxxxxx.....]
            # [....xxxx.......]
            if first[0] <= second[0] and first[1] >= second[1]:
                contained += 1
                continue

            # [....xxxx.......]
            # [...xxxxxxx.....]
            if first[0] >= second[0] and first[1] <= second[1]:
                contained += 1
                continue

        return contained

    @property
    def part_2_solution(self) -> int:
        return 903
