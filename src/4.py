"""
See: https://adventofcode.com/2021/day/4
"""
from typing import List



def parse_input():
    with open('input/4.txt', 'r') as file:
        lines = file.read().split('\n')
    draw_nums: List[int] = [int(x) for x in lines[0].split(',')]

    boards: List[List[List[int]]] = []
    curr_board: List[List[int]] = []
    for i in range(2,len(lines)):
        if lines[i] == '':
            # end of card chunk
            boards.append(curr_board)
            curr_board: List[List[int]] = []
        else:
            tokens: List[str] = lines[i].split(' ')
            curr_board.append([int(n) for n in filter(remove_empty, tokens)])
    
    return draw_nums, boards

def remove_empty(var):
    if var == '':
        return False
    return True

def part2() -> int:
    draw_q, boards = parse_input()
    drawed_nums: List[int] = []

    winner_board = None
    while not winner_board:
        if len(boards) == 1: # stop searching for bingo if only 1 board remaining - this is the last winner
            winner_board = boards[0]
            break
        
        drawed_nums.append(draw_q.pop(0))

        for b in boards:        
            # check horizontal bingo
            for row in b:
                for idx, num in enumerate(row):
                    if num not in drawed_nums:
                        break
                    if idx == 4 and b in boards: # make sure we dont remove it twice
                        boards.remove(b)                

            # check vertical bingo
            for col in range(5):
                for row in range(5):
                    if b[row][col] not in drawed_nums:
                        break
                    if row == 4 and b in boards: # make sure we dont remove it twice
                        boards.remove(b)

    for winner_num in draw_q:
        drawed_nums.append(winner_num)
        for row in winner_board:
            if winner_num in row:
                break
        else: # this weird syntax breaks out of nested loops: https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops
            continue
        break

    # compute final score
    final_score: int = 0

    for row in winner_board:
        for num in row:
            if num not in drawed_nums:
                final_score += num
                
    return final_score * winner_num

def part1() -> int:
    draw_q, boards = parse_input()
    drawed_nums: List[int] = []

    winner_num = None
    winner_board = None
    while not winner_board:
        drawed_nums.append(draw_q.pop(0))

        for b in boards:
            # check horizontal bingo
            for row in b:
                for idx, num in enumerate(row):
                    if num not in drawed_nums:
                        break
                    if idx == 4:
                        winner_board = b
                        winner_num = drawed_nums[-1]

            # check vertical bingo
            for col in range(5):
                for row in range(5):
                    if b[row][col] not in drawed_nums:
                        break
                    if row == 4:
                        winner_board = b
                        winner_num = drawed_nums[-1]

    # compute final score
    final_score: int = 0

    for row in winner_board:
        for num in row:
            if num not in drawed_nums:
                final_score += num

    return final_score * winner_num
    


if __name__ == '__main__':
    print(part2())
