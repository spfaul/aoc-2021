"""
See: https://adventofcode.com/2021/day/10

LMFAO they really just rephrased matching parenthesis
"""
from typing import *

def parse_input() -> List[List[str]]:
    data: List[List[str]] = []
    with open('input/10.txt', 'r') as file:
        for line in file.read().split('\n'):
            data.append([char for char in line])
    return data

def part1() -> int:
    VALID_BRACKETS: Dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
    BRACKET_TO_POINTS: Dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}
    data: List[List[str]] = parse_input()
    point_total: int = 0

    for chunk in data:
        stack: List[str] = []
        
        for bracket in chunk:
            if bracket in VALID_BRACKETS.keys(): # opening brackeys
                stack.append(bracket)
                continue
                
            # closing brackets
            if VALID_BRACKETS[stack[-1]] == bracket: # valid
                stack.pop()
            else: # corrupted
                point_total += BRACKET_TO_POINTS[bracket]
                break

    return point_total

def part2() -> int:
    VALID_BRACKETS: Dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
    BRACKET_TO_POINTS: Dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}
    data: List[List[str]] = parse_input()
    scores: List[int] = []

    for chunk in data:
        stack: List[str] = []
        score: int = 0
        corrupted: bool = False

        for bracket in chunk:
            # open brackeys
            if bracket in VALID_BRACKETS.keys():
                stack.append(bracket)
                continue
                
            # closing brackeys
            if VALID_BRACKETS[stack[-1]] == bracket: # valid
                stack.pop()
            else: # corrupted, so skip to next chunk
                corrupted = True
                break
                
        if corrupted:
            continue
            
        # remaining brackeys in stack are incomplete
        stack.reverse() # start from last opening brackey
        for opener in stack:
            score *= 5
            score += BRACKET_TO_POINTS[VALID_BRACKETS[opener]]

        scores.append(score)

    # get middle score
    scores.sort()
    return scores[int(len(scores) / 2)]

if __name__ == '__main__':
    print(part2())