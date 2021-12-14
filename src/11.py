"""
See: https://adventofcode.com/2021/day/11

dumbo octopus!!
"""
from typing import *
from pprint import pprint

def parse_input() -> List[List[int]]:
    with open("input/11.txt", "r") as file:
        return [[int(i) for i in line] for line in file.read().split('\n')]

def part1() -> int:
    data: List[List[int]] = parse_input()
    flash_count: int = 0

    for i in range(100):
        flashed_octo: List[Tuple[int, int]] = []
        for y in range(10):
            for x in range(10):
                data, flashed_octo, flash_count = tick_a(data, x, y, flashed_octo, flash_count)

    return flash_count


def part2() -> int:
    data: List[List[int]] = parse_input()
    flash_count: int = 0

    for i in range(1000):
        flashed_octo: List[Tuple[int, int]] = []
        for y in range(10):
            for x in range(10):
                data, flashed_octo, flash_count = tick_a(data, x, y, flashed_octo, flash_count)

                if flash_sync(data):
                    return i+1

def flash_sync(data: List[List[int]]):
    for line in data:
        for num in line:
            if num != 0:
                return False
    return True


def tick_a(data: List[List[int]], x: int, y: int, flashed_list: List[Tuple[int, int]], flash_count: int):
    if x < 0 or x > len(data[0]) - 1 or y < 0 or y > len(data) - 1:
        return data, flashed_list, flash_count
    
    energy: int = data[y][x]
    if energy == 0 and (x, y) in flashed_list:
        return data, flashed_list, flash_count
        
    if energy == 9:
        data[y][x] = 0
        flash_count += 1
        flashed_list.append((x, y))
        for x_offset, y_offset in [(-1,-1), (-1,0), (-1,1), (1,1), (0,1), (1,0), (0,-1), (1,-1)]:
            data, flashed_list, flash_count = tick_a(data, x + x_offset, y + y_offset, flashed_list, flash_count)
    else:
        data[y][x] += 1

    return data, flashed_list, flash_count

if __name__ == '__main__':
    print(part2())
