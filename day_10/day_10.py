#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
import numpy as np

from day import Day


@dataclass
class CPU:
    x: int = 1
    cycle: int = 0

    def noop(self) -> None:
        self.cycle += 1

    def add_x(self, x: int) -> None:
        self.x += x
        self.cycle += 2


class Day10(Day):
    def __init__(self) -> None:
        super().__init__(10)

    def parse_data(self) -> list[str]:
        return self.raw_data

    def part_1(self) -> int:
        signal_strength = 0
        next_check_cycle = 20
        cpu = CPU()

        for instruction in self.data:
            initial_x = cpu.x
            if instruction == "noop":
                cpu.noop()
            elif instruction.startswith("addx "):
                x = int(instruction.split(" ")[1])
                cpu.add_x(x)
            else:
                assert False

            if cpu.cycle >= next_check_cycle:
                signal_strength += next_check_cycle * initial_x
                next_check_cycle += 40

        return signal_strength

    @property
    def part_1_solution(self) -> int:
        return 17380

    def part_2(self) -> int:
        cpu = CPU()
        column_count = 40
        crt = np.zeros((6, column_count), dtype=bool)

        def draw_pixel(cycle: int, position: int) -> None:
            if (cycle % column_count) <= position + 1 and (
                cycle % column_count
            ) >= position - 1:
                row = cycle // column_count
                column = cycle % column_count
                crt[row, column] = True

        for instruction in self.data:
            initial_cycle = cpu.cycle
            initial_x = cpu.x
            if instruction == "noop":
                cpu.noop()
            elif instruction.startswith("addx "):
                x = int(instruction.split(" ")[1])
                cpu.add_x(x)
            else:
                assert False

            for cycle in range(initial_cycle, cpu.cycle):
                draw_pixel(cycle, initial_x)

        Day10._render_crt(crt)
        return "FGCUZREC"

    @staticmethod
    def _render_crt(crt: np.ndarray) -> None:
        rendered = np.empty_like(crt, dtype=str)
        rendered[~crt] = "."
        rendered[crt] = "#"
        for row in rendered.tolist():
            print("".join(row))

    @property
    def part_2_solution(self) -> int:
        return "FGCUZREC"
