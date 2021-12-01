"""
part 1: https://adventofcode.com/2021/day/1
part 2: https://adventofcode.com/2021/day/1#part2
"""

from typing import NoReturn, List

def get_puzzle_input() -> List[int]:
    with open('input/1.txt', 'r') as file:
        return [int(line) for line in file.read().split('\n')]


def part1() -> int:
    data: List[int] = get_puzzle_input()
    count: int = 0

    for idx, n in enumerate(data):
        if idx == 0:
            continue
        if n > data[idx-1]:
            count += 1

    return count

def part2() -> int:
    data: List[int] = get_puzzle_input()
    data_len: int = len(data)
    count: int = 0

    for idx, n in enumerate(data):
        if idx > data_len - 1 - 3:
            return count
        if data[idx] + data[idx+1] + data[idx+2] < data[idx+1] + data[idx+2] + data[idx+3]:
            count += 1
        

if __name__ == '__main__':
    print(part2())
