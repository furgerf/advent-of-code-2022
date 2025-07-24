#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day

Stack = list[str]
Instruction = tuple[int, int, int]


class Day5(Day):
    def __init__(self) -> None:
        super().__init__(5)

    def parse_data(self) -> tuple[list[Stack], list[Instruction]]:
        empty_line_index = self.raw_data.index("")
        stack_count = len(
            [stack for stack in self.raw_data[empty_line_index - 1].split(" ") if stack]
        )
        stacks = [[] for _ in range(stack_count)]
        for i in range(empty_line_index - 1):
            for j in range(stack_count):
                crate = self.raw_data[i][j * 4 : j * 4 + 3]
                if crate.strip():
                    stacks[j].insert(0, crate)

        instructions = []
        for instruction in self.raw_data[empty_line_index + 1 :]:
            split_instruction = instruction.split(" ")
            instructions.append(
                (
                    int(split_instruction[1]),
                    int(split_instruction[3]) - 1,
                    int(split_instruction[5]) - 1,
                )
            )

        return stacks, instructions

    def part_1(self) -> int:
        stacks, instructions = self.data
        for count, source, destination in instructions:
            for _ in range(count):
                crate = stacks[source].pop()
                stacks[destination].append(crate)

        return "".join(stack[-1].strip("[]") for stack in stacks)

    @property
    def part_1_solution(self) -> int:
        return "FWSHSPJWM"

    def part_2(self) -> int:
        stacks, instructions = self.data
        for count, source, destination in instructions:
            crates = []
            for _ in range(count):
                crates.insert(0, stacks[source].pop())
            stacks[destination].extend(crates)

        return "".join(stack[-1].strip("[]") for stack in stacks)

    @property
    def part_2_solution(self) -> int:
        return "PWPWHGFZS"
