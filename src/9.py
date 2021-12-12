"""
See: https://adventofcode.com/2021/day/9
"""
from typing import *
from functools import reduce

def parse_input() -> List[List[int]]:
    data: List[List[int]] = []
    with open('input/9.txt', 'r') as file:
        contents = file.read()
        for line in contents.split("\n"):
            data.append([int(char) for char in line])
    return data

 
def part1() -> int:
    # Brute force approach, as always
    data: List[List[int]] = parse_input()
    # print(data)
    risk_level_sum: int = 0
    
    for y, row in enumerate(data):
        for x, n in enumerate(row):
            # adj left
            if x > 0 and n >= data[y][x-1]:
                continue
            # adj right
            if len(row) - 1 > x and n >= data[y][x+1]:
                continue
            # adj up
            if y > 0 and n >= data[y-1][x]:
                continue
            # adj down
            if len(data) - 1 > y and n >= data[y+1][x]:
                continue
            # low point, add to sum
            risk_level_sum += n + 1
            
    return risk_level_sum
    

def part2() -> int:
    data: List[List[int]] = parse_input()
    basins_len: List[int] = []
    already_in_basin: List[Tuple[int, int]] = []

    for y, row in enumerate(data):
        for x, n in enumerate(row):
            if (x, y) in already_in_basin:
                continue
        
            basin = get_basin(data, x, y)
            if basin != []:
                basins_len.append(len(basin))
                already_in_basin += basin

    basins_len.sort()
    three_biggest_basin_lens: List[int] = basins_len[-3:]
    
    return reduce(lambda x, y: x * y, three_biggest_basin_lens, 1)
    
def get_basin(grid: List[List[int]], x: int, y: int, basin: List[Tuple[int, int]] = None):
    if basin == None:
        basin = [] # python hates lists as default params, so this is a workaround

    if grid[y][x] == 9:
        return basin

    basin.append((x, y))
    # adj left
    if x > 0 and (x-1, y) not in basin:
        basin = get_basin(grid, x-1, y, basin)
    # adj right
    if len(grid[0]) - 1 > x and (x+1, y) not in basin:
        basin = get_basin(grid, x+1, y, basin)
    # adj up
    if y > 0 and (x, y-1) not in basin:
        basin = get_basin(grid, x, y-1, basin)
    # adj down
    if len(grid) - 1 > y and (x, y+1) not in basin:
        basin = get_basin(grid, x, y+1, basin)

    return basin
    
    

if __name__ == '__main__':
    print(part2())
