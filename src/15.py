"""
See: https://adventofcode.com/2021/day/15
Basically a maze traversing algo implementation

DIDNT MANAGE TO FIND AN ANSWER, IGNORE THIS FILE - IT'S GARBAGE
"""
from typing import *
import sys

sys.setrecursionlimit(10000000)


def parse_input() -> List[List[int]]:
    with open('input/test_test_15.txt', 'r') as file:
        return [[int(c) for c in line] for line in file.read().split("\n")]

def part1():
    data: List[List[int]] = parse_input()

    lowest_risk: int = traverse1(data, 0, 0, 0)

    return lowest_risk

def traverse1(maze: List[List[int]], x: int, y: int, risk: int, cache: Dict[Tuple[int, int], int] = None, prev: List[Tuple[int, int]] = None) -> int:
    if cache == None:
        cache = {} # python hates dicts and arrays as default params
    if prev == None:
        prev = []

    min_risk: int = 100000 # random arbitrarily large number
    risk_left, risk_right = 1000001, 10000001
            
    if x != 0 or y != 0:
        risk += maze[y][x]
    if x == len(maze[0]) - 1 and y == len(maze) - 1:
        return risk


    prev.append((x, y))


    if len(maze[0]) - 1 > x and (x+1, y) not in prev:
        if (x + 1, y) in cache.keys():
            min_risk = min(min_risk, cache[(x+1, y)] + risk)
        else:
            risk_right: int = traverse1(maze, x+1, y, 0, cache, prev.copy())
            min_risk = min(min_risk, risk_right + risk)
        
    if len(maze) - 1 > y and (x, y+1) not in prev:
        if (x, y + 1) in cache.keys():
            min_risk = min(min_risk, cache[(x, y+1)] + risk)
        else:
            risk_down: int = traverse1(maze, x, y+1, 0, cache, prev.copy())
            min_risk = min(min_risk, risk_down + risk)

    if x > 0 and (x-1, y) not in prev:
        if (x - 1, y) in cache.keys():
            min_risk = min(min_risk, cache[(x-1, y)] + risk)
        else:
            risk_left: int = traverse1(maze, x-1, y, 0, cache, prev.copy())
            min_risk = min(min_risk, risk_left + risk)

    if y > 0 and (x, y-1) not in prev:
        if (x, y-1) in cache.keys():
            min_risk = min(min_risk, cache[(x, y-1)] + risk)
        else:
            risk_up: int = traverse1(maze, x, y-1, 0, cache, prev.copy())
            min_risk = min(min_risk, risk_up + risk)

    if (x, y) not in cache.keys() or min(min_risk, cache[(x, y)]) == min_risk: 
        if x == 3 and y == 1:
            print(min_risk, risk_right, prev)
        cache[(x, y)] = min_risk

    # print(cache)
    return min_risk

if __name__ == "__main__":
    print(part1())
