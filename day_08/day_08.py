#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from day import Day


class Day8(Day):
    def __init__(self) -> None:
        super().__init__(8)

    def parse_data(self) -> np.ndarray:
        return np.array([list(row) for row in self.raw_data], dtype=int)

    def part_1(self) -> int:
        visible = 0
        for index in np.ndindex(self.data.shape):
            visible += int(self._is_visible(*index))

        return visible

    def _is_visible(self, i: int, j: int) -> bool:
        if (self.data[:i, j] < self.data[i, j]).all():
            return True
        if (self.data[i + 1 :, j] < self.data[i, j]).all():
            return True
        if (self.data[i, :j] < self.data[i, j]).all():
            return True
        if (self.data[i, j + 1 :] < self.data[i, j]).all():
            return True

        return False

    @property
    def part_1_solution(self) -> int:
        return 1546

    def part_2(self) -> int:
        score = 0
        for index in np.ndindex(self.data.shape):
            score = max(score, self._scenic_score(*index))

        return score

    def _scenic_score(self, i: int, j: int) -> int:
        count_left = Day8._count_visible_trees(
            np.flip((self.data[:i, j]) < self.data[i, j])
        )
        count_right = Day8._count_visible_trees(self.data[i + 1 :, j] < self.data[i, j])
        count_top = Day8._count_visible_trees(
            np.flip(self.data[i, :j]) < self.data[i, j]
        )
        count_bottom = Day8._count_visible_trees(
            self.data[i, j + 1 :] < self.data[i, j]
        )
        return count_left * count_right * count_top * count_bottom

    @staticmethod
    def _count_visible_trees(array: np.ndarray) -> int:
        indexes = np.where(~array)[0]
        result = indexes[0] + 1 if len(indexes) else len(array)
        return result

    @property
    def part_2_solution(self) -> int:
        return 519064
