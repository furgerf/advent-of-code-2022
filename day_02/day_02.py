#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from day import Day


class Day2(Day):
    def __init__(self) -> None:
        super().__init__(2)

    def parse_data(self) -> np.ndarray:
        return np.array([Day2._parse_row(row) for row in self.raw_data])

    @staticmethod
    def _parse_row(row: str) -> tuple[int, int]:
        theirs, mine = row.split()
        return ({"A": 1, "B": 2, "C": 3}[theirs], {"X": 1, "Y": 2, "Z": 3}[mine])

    def part_1(self) -> int:
        result_score = sum(Day2._score_for_outcome(*row) for row in self.data)
        own_score = self.data[:, 1].sum()
        return result_score + own_score

    @staticmethod
    def _score_for_outcome(theirs: int, mine: int) -> int:
        if theirs == mine:
            return 3
        if (theirs + 1) % 3 == mine % 3:  # values are 1-based but modulo is 0-based
            return 6
        return 0

    @property
    def part_1_solution(self) -> int:
        return 13052

    def part_2(self) -> int:
        mine = [Day2._calculate_my_hand(*turn) for turn in self.data]
        result_score = sum(
            Day2._score_for_outcome(*row) for row in zip(self.data[:, 0], mine)
        )
        own_score = sum(mine)
        return result_score + own_score

    @staticmethod
    def _calculate_my_hand(theirs: int, outcome: int) -> int:
        # lose, tie, win
        if outcome == 2:
            return theirs

        if outcome == 3:
            return theirs % 3 + 1

        return (theirs + 1) % 3 + 1

    @property
    def part_2_solution(self) -> int:
        return 13693
