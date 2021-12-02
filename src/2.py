"""
See: https://adventofcode.com/2021/day/2
"""
from typing import List

def parse_input() -> List[str]:
    with open("input/2.txt", "r") as file:
        return file.read().split("\n")

def part1() -> int:
    x_pos: int = 0
    depth: int = 0
    instructions: List[str] = parse_input()
    
    for command in instructions:
        val: int = int(command.split(" ")[1])
    
        if command.startswith("forward"):
            x_pos += val
        elif command.startswith("down"):
            depth += val
        else:
            depth -= val

    return x_pos * depth

def part2() -> int:
    aim: int = 0
    x_pos: int = 0
    depth: int = 0
    instructions: List[str] = parse_input()

    for command in instructions:
        val: int = int(command.split(" ")[1])

        if command.startswith("forward"):
            x_pos += val
            depth += aim * val
        elif command.startswith("down"):
            aim += val
        else:
            aim -= val

    return x_pos * depth


if __name__ == "__main__":
    print(part2())