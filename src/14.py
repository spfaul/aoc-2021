"""
See: https://adventofcode.com/2021/day/14

Needed hints from aoc's subreddit. Optimizing algorithms is not for me :(
"""

from typing import *
from collections import defaultdict

def parse_input() -> Tuple[str, Dict[str, str]]:
    with open("input/14.txt", "r") as file:
        inserts: Dict[str, str] = {}
        for idx, line in enumerate(file.read().split('\n')):
            if idx == 0:
                template: str = line
            elif line != "":
                pair, insert_char = line.split(" -> ")
                inserts[pair] = insert_char

    return template, inserts

def bothparts() -> int:
    template, inserts = parse_input()

    pair_count: defaultdict = defaultdict(int)
    char_count: defaultdict = defaultdict(int)
    
    # extract pairs from template
    for idx, char in enumerate(template[:-1]):
        pair_count[template[idx:idx+2]] += 1
        char_count[char] += 1
    char_count[template[-1]] += 1
    
    for i in range(40): # set range to 10 for part1, 40 for part2 
        for pair, count in list(pair_count.items()):
            if pair in inserts.keys():
                insert_char: str = inserts[pair]
            else:
                insert_char: str = ""
                
            char_count[insert_char] += count
            pair_count[pair[0] + insert_char] += count
            pair_count[insert_char + pair[1]] += count
                
            pair_count[pair] -= count
        
    return max(char_count.values()) - min(char_count.values())


if __name__ == '__main__':
    print(bothparts())