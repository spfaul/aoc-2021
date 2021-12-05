"""
See: https://adventofcode.com/2021/day/5

dont even try to read this, its all spaghetti
"""

def parse_input():
    with open("input/5.txt") as file:
        contents = file.read().split('\n')

    vents = []
    for vent_info in contents:
        entry, _, exit = vent_info.split(' ')
        entry_pos = [int(n) for n in entry.split(',')]
        exit_pos = [int(n) for n in exit.split(',')]        
        distance = [exit_pos[0] - entry_pos[0], exit_pos[1] - entry_pos[1]]

        # UNCOMMENT FOR PART 1 TO WORK
        # if 0 not in distance: # part 1 doesnt consider diagnal changes
            # continue

        if distance[0] > 0 or distance[1] > 0 or abs(distance[0]) == abs(distance[1]):        
            vents.append([entry_pos, distance])
        else:
            vents.append([exit_pos, distance])

    return vents

def part1():
    data = parse_input()
    grid = {}

    for pos, change in data:
        axis = int(change[0] == 0) # 0 - moving to the right
                                    # 1 - moving downwards
                                    
        # equivalent to range(entry.axis, exit.axis + 1) if exit is below/to the right of entry_pos
        for i in range(pos[axis], pos[axis] + abs(change[axis]) + 1): 
            if axis == 0:
                pos_str = f'{i};{pos[1]}'
            else:
                pos_str = f'{pos[0]};{i}'

            if pos_str not in grid.keys():
                grid[pos_str] = 1
            else:
                grid[pos_str] += 1

    overlaps = 0
    for val in grid.values():
        if val > 1:
            overlaps += 1

    return overlaps

def part2():
    data = parse_input()
    grid = {}

    for pos, change in data:
        if abs(change[0]) == abs(change[1]):
            # diagnal
            x, y = pos
            for i in range(abs(change[0]) + 1):
                pos_str = f'{int(x)};{int(y)}'
                
                if pos_str not in grid.keys():
                    grid[pos_str] = 1
                else:
                    grid[pos_str] += 1
                    
                x += change[0] / abs(change[0])
                y += change[1] / abs(change[1])
            continue
    
    
        axis = int(change[0] == 0) # 0 - moving to the right
                                    # 1 - moving downwards
                                    
        # equivalent to range(entry.axis, exit.axis + 1) if exit is below/to the right of entry_pos
        for i in range(pos[axis], pos[axis] + abs(change[axis]) + 1): 
            if axis == 0:
                pos_str = f'{i};{pos[1]}'
            else:
                pos_str = f'{pos[0]};{i}'

            if pos_str not in grid.keys():
                grid[pos_str] = 1
            else:
                grid[pos_str] += 1

    overlaps = 0
    for val in grid.values():
        if val > 1:
            overlaps += 1

    return overlaps



def print_grid(grid):
    # for debugging purposes, only prints x=0-9 and y=0-9 of grid
    for y in range(10):
        line = ""
        for x in range(10):
            if f'{x};{y}' not in grid.keys():
                line += '.'
            else:
                line += str(grid[f'{x};{y}'])
        print(line)

if __name__ == '__main__':
    print(part2())
