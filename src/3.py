"""
See: https://adventofcode.com/2021/day/3
"""
from typing import List

def parse_input() -> List[str]:
    with open("input/3.txt", "r") as file:
        return file.read().split("\n")

def binary_to_decimal(bin_repr: str) -> int:
    return int(bin_repr, 2)

def part1() -> int:
    data: List[str] = parse_input()
    gamma_rate: str = ""
    epsilon_rate: str = ""

    col: int
    for col in range(len(data[0])):
        zero_count: int = 0;

        num: str
        for num in data:
            if num[col] == '0':
                zero_count += 1

        if zero_count > len(data)//2:
            # 0 is most common bit
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            # 1 is most common bit
            gamma_rate += '1'
            epsilon_rate += '0'
    
    return binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate)

def get_bit_popularity(x: List[str], bit_idx: int) -> tuple[List[str], List[str]]:
    zero_bits = []
    one_bits = []
    for num in x:
        if num[bit_idx] == '0':
            zero_bits.append(num)
        else:
            one_bits.append(num)

    return zero_bits, one_bits
    

def part2() -> int:
    data: List[str] = parse_input()
    oxy_possible: List[str] = data.copy()
    carbon_possible: List[str] = data.copy()

    for col in range(len(data[0])):
        if len(oxy_possible) == 1 and len(carbon_possible) == 1:
            break

        # this solution is just... yikes. there probably is a cleaner solution, but as long as it works, right?
        
        if len(oxy_possible) > 1:
            zero_bit, one_bit = get_bit_popularity(oxy_possible, col)
                      
            if len(one_bit) == len(zero_bit) or len(one_bit) > len(zero_bit):
                oxy_possible = one_bit.copy()
            else:
                oxy_possible = zero_bit.copy()

        if len(carbon_possible) > 1:
            zero_bit, one_bit = get_bit_popularity(carbon_possible, col)
            
            if len(one_bit) == len(zero_bit) or len(one_bit) > len(zero_bit):
                carbon_possible = zero_bit.copy()
            else:
                carbon_possible = one_bit.copy()

    return binary_to_decimal(oxy_possible[0]) * binary_to_decimal(carbon_possible[0])

if __name__ == '__main__':
    print(part2())
