"""
See: https://adventofcode.com/2021/day/13

forced myself to use curses because idw to deal with ansi escape codes or GUIs today.
reject bloat, return to curses.
"""

from typing import *
import curses

def parse_input() -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    dots: List[Tuple[int, int]] = []
    folds: List[Tuple[str, int]] = []

    with open('input/13.txt', 'r') as file:
        for line in file.read().split('\n'):
            if line.startswith('fold along'):
                axis, pos = line.replace("fold along ", "").split("=")
                folds.append((axis, int(pos)))
            elif line != "":
                x, y = line.split(',')
                dots.append((int(x), int(y)))
                
    return (dots, folds)

def part1() -> int:
    dots, folds = parse_input()
    paper: Dict[Tuple[int, int], bool] = {}

    for dot in dots:
        paper[dot] = True

    axis, fold_amnt = folds[0]
    for pos, val in paper.copy().items():
        x, y = pos
        if axis == "y" and y > fold_amnt:
            del paper[pos]
            paper[(x, fold_amnt - (y - fold_amnt))] = True
        elif axis == "x" and x > fold_amnt:
            del paper[pos]
            paper[( fold_amnt - (x - fold_amnt)), y] = True    

    return len(list(paper.values()))

def part2() -> int:
    dots, folds = parse_input()
    paper: Dict[Tuple[int, int], bool] = {}

    for dot in dots:
        paper[dot] = True

    for fold in folds:
        axis, fold_amnt = fold
        for pos, val in paper.copy().items():
            x, y = pos
            if axis == "y" and y > fold_amnt:
                del paper[pos]
                paper[(x, fold_amnt - (y - fold_amnt))] = True
            elif axis == "x" and x > fold_amnt:
                del paper[pos]
                paper[( fold_amnt - (x - fold_amnt)), y] = True

    display_dots(paper)

def display_dots(paper: Dict[Tuple[int, int], bool]):
    def display_loop(stdscr):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        for pos in paper.keys():
            x, y = pos
            stdscr.addch(y, x, "#")
        stdscr.refresh()
        stdscr.getch()

    curses.wrapper(display_loop)


if __name__ == '__main__':
    print(part2())
