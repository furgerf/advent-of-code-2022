#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day
from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: "Directory | None"
    files: list[File] = field(default_factory=lambda: [])
    directories: list["Directory"] = field(default_factory=lambda: [])

    @property
    def size(self) -> int:
        files_size = sum(file.size for file in self.files)
        directories_size = sum(directory.size for directory in self.directories)
        return files_size + directories_size

    def get_directory(self, name: str) -> "Directory | None":
        for directory in self.directories:
            if directory.name == name:
                return directory

        return None


class Day7(Day):
    def __init__(self) -> None:
        super().__init__(7)

    def parse_data(self) -> Directory:
        root = Directory("/", None)
        cwd = root
        for line in self.raw_data:
            if line.startswith("$ cd"):
                destination = line[5:]
                if destination == "/":
                    cwd = root
                elif destination == "..":
                    assert cwd.parent
                    cwd = cwd.parent
                else:
                    assert (directory := cwd.get_directory(destination))
                    cwd = directory
            elif line == "$ ls":
                pass
            elif line.startswith("dir "):
                name = line[line.index(" ") + 1 :]
                cwd.directories.append(Directory(name, cwd))
            elif str.isnumeric(line[: line.index(" ")]):
                size_str, name = line.split(" ", 2)
                cwd.files.append(File(name, int(size_str)))
            else:
                raise NotImplementedError()

        return root

    def part_1(self) -> int:
        return sum(
            directory.size
            for directory in Day7._find_small_directories(self.data, 100000, None)
        )

    @staticmethod
    def _find_small_directories(
        cwd: Directory, max_size: int | None, min_size: int | None
    ) -> list[Directory]:
        directories: list[Directory] = []
        if max_size is not None and cwd.size <= max_size:
            directories.append(cwd)
        if min_size is not None and cwd.size >= min_size:
            directories.append(cwd)

        for directory in cwd.directories:
            directories.extend(
                Day7._find_small_directories(directory, max_size, min_size)
            )
        return directories

    @property
    def part_1_solution(self) -> int:
        return 1642503

    def part_2(self) -> int:
        total_size = 70000000
        required_size = 30000000
        used_size = self.data.size
        return min(
            directory.size
            for directory in Day7._find_small_directories(
                self.data, None, required_size - total_size + used_size
            )
        )

    @property
    def part_2_solution(self) -> int:
        return 6999588
