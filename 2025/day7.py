#!/usr/bin/env python3

# https://adventofcode.com/2024/day/7

import argparse
from enum import Enum

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day7.txt')

class Element(Enum):
    EMPTY = 1
    SPLITTER = 2
    BEAM = 3

    def get(ch):
        if ch == '.':
            return Element.EMPTY
        elif ch == '^':
            return Element.SPLITTER
        elif ch == 'S':
            return Element.BEAM
        else:
            raise Exception("Unknown element")
        
class State:
    def __init__(self, inputfile):
        self.grid = [[Element.get(ch) for ch in line.strip()] for line in inputfile]
        self.height = len(self.grid)
        self.width = len(self.grid[0])
    
    def in_bounds(self, row, col) -> bool:
        return not (row < 0 or col < 0 or row >= self.height or col >= self.width)
    
    def try_mark_beam(self, row, col) -> bool:
        if not self.in_bounds(row, col):
            return False
        elif self.grid[row][col] == Element.EMPTY:
            self.grid[row][col] = Element.BEAM
            return True
        else:
            return False

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    state = State(inputfile)
    splits = 0
    # Process each row from the top down
    for y, row in enumerate(state.grid):
        for x, element in enumerate(row):
            if element == Element.BEAM:
                # Try to propogate the beam down
                state.try_mark_beam(y+1, x)
            elif element == Element.SPLITTER:
                # First check if we had a beam above
                if state.in_bounds(y-1, x) and state.grid[y-1][x] == Element.BEAM:
                    # Try to progagate the beam down twice
                    splits += 1
                    state.try_mark_beam(y+1, x-1)
                    state.try_mark_beam(y+1, x+1)
    return splits

class QuantumElement:
    def __init__(self, element):
        self.element = element
        self.count = 1 if element == Element.BEAM else 0


class QuantumState:
    def __init__(self, inputfile):
        self.grid = [[QuantumElement(Element.get(ch)) for ch in line.strip()] for line in inputfile]
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def in_bounds(self, point):
        row = point[0]
        col = point[1]
        return not (row < 0 or col < 0 or row >= self.height or col >= self.width)
    
    def get_element(self, point) -> QuantumElement:
        return self.grid[point[0]][point[1]]
    
    def set_beams(self, point, count: int):
        e = self.grid[point[0]][point[1]]
        e.element = Element.BEAM
        e.count += count
    
    def try_mark_beam(self, next, source):
        if not self.in_bounds(next):
            return
        next_element = self.get_element(next)
        if next_element.element != Element.SPLITTER:
            self.set_beams(next, self.get_element(source).count)

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    state = QuantumState(inputfile)
    # Process each row from the top down
    for y, row in enumerate(state.grid):
        for x, qe in enumerate(row):
            if qe.element == Element.BEAM:
                # Try to propogate the beams down
                state.try_mark_beam((y+1, x), (y,x))
            elif qe.element == Element.SPLITTER:
                # First check if we had a beam above
                previous = (y-1, x)
                if state.in_bounds(previous) and state.get_element(previous).element == Element.BEAM:
                    state.try_mark_beam((y+1, x-1), previous)
                    state.try_mark_beam((y+1, x+1), previous)
    # Now count the number of timelines on the last row
    timelines = 0
    y = len(state.grid) - 1
    for element in state.grid[y]:
        timelines += element.count
    return timelines

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
