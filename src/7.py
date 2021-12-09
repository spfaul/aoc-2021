from typing import List, Union

def parse_input() -> List[int]:
    with open('input/7.txt', 'r') as file:
        return [int(n) for n in file.read().split(',')]
 
def part1() -> int:
    data: List[int] = parse_input()

    min_fuel_spent: Union[int, None] = None

    for n in range(min(data), max(data)+1):
        tmp_fuel: int = 0
        for pos in data:
            tmp_fuel += abs(pos-n)

        if min_fuel_spent == None:
            min_fuel_spent = tmp_fuel
            continue
            
        min_fuel_spent = min(min_fuel_spent, tmp_fuel)

    return min_fuel_spent

def part2() -> int:
    def dist_to_fuel(dist: int) -> int:
        return int(dist * (dist + 1) / 2) # simple algo to find sum of 1 to dist

    data: List[int] = parse_input()
    min_fuel_spent: Union[int, None] = None

    for n in range(min(data), max(data)+1):
        tmp_fuel: int = 0

        for pos in data:
            tmp_fuel += dist_to_fuel(abs(pos-n))

        if min_fuel_spent == None:
            min_fuel_spent = tmp_fuel
            continue
            
        min_fuel_spent = min(min_fuel_spent, tmp_fuel)

    return min_fuel_spent


if __name__ == '__main__':
    print(part2())
