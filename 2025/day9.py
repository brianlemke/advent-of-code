#!/usr/bin/env python3

# https://adventofcode.com/2024/day/9

import argparse
from enum import Enum

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day9.txt')

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    reds = [tuple([int(num) for num in line.strip().split(',')]) for line in inputfile]
    largest = 0
    for i in range(len(reds) - 1):
        a = reds[i]
        for j in range(i + 1, len(reds)):
            b = reds[j]
            size = (abs(a[0] - b[0])+1) * (abs(a[1] - b[1])+1)
            if size > largest:
                largest = size
    return largest

class Tile(Enum):
    RED = 1
    GREEN = 2
    UNKNOWN = 3

class CompactedGrid:
    def __init__(self, reds:list[tuple[int,int]]):
        # Build a compacted grid
        def compact_line(values) -> dict[int, int]:
            mapping = {}
            unique_sorted = sorted(list(set(values)))
            for i, v in enumerate(unique_sorted):
                mapping[v] = i
            return mapping
        self.map_x = compact_line([r[0] for r in reds])
        self.map_y = compact_line([r[1] for r in reds])

        self.grid:list[list[Tile]] = []

        # Start by making an empty grid
        for y in range(0, len(self.map_y)):
            row = []
            self.grid.append(row)
            for x in range(0, len(self.map_x)):
                row.append(Tile.UNKNOWN)

        # Fill in the edges
        reds.append(reds[0]) # For wrap-around
        cprev = self.compact_point(reds[0])
        self.grid[cprev[1]][cprev[0]] = Tile.RED
        for n in reds[1:]:
            cnext = self.compact_point(n)
            if cnext[0] != cprev[0]: # Horizontal
                y = cnext[1]
                step = -1 if cnext[0] < cprev[0] else 1
                for x in range(cprev[0], cnext[0]+step, step):
                    if (x,y) in reds:
                        self.grid[y][x] = Tile.RED
                    else:
                        self.grid[y][x] = Tile.GREEN
            else:                  # Vertical
                x = cnext[0]
                step = -1 if cnext[1] < cprev[1] else 1
                for y in range(cprev[1], cnext[1]+step, step):
                    if (x,y) in reds:
                        self.grid[y][x] = Tile.RED
                    else:
                        self.grid[y][x] = Tile.GREEN
            cprev = cnext

        # Fill in the center
        # Scan lines from left to right. If we ever see a pattern of [RG] -> [U] -> [RG] then 
        # we toggle the "inside" state
        for y, row in enumerate(self.grid):
            inside = False
            last_unknown = True
            for x, item in enumerate(row):
                if item == Tile.UNKNOWN:
                    last_unknown = True
                    self.grid[y][x] = Tile.GREEN if inside else Tile.UNKNOWN
                elif last_unknown:
                    last_unknown = False
                    inside = not inside

    def compact_point(self, point:tuple[int,int]):
        return (self.map_x[point[0]], self.map_y[point[1]])
    
    def check_box(self, a:tuple[int,int], b:tuple[int,int]):
        """Check if every compacted point is colored properly"""
        ca = self.compact_point(a)
        cb = self.compact_point(b)

        # Check each point in the box
        xstep = 1 if ca[0] <= cb[0] else -1
        ystep = 1 if ca[1] <= cb[1] else -1
        for x in range(ca[0], cb[0]+xstep, xstep):
            for y in range(ca[1], cb[1]+ystep, ystep):
                if self.grid[y][x] == Tile.UNKNOWN:
                    return False
        return True

    def print(self):
        print()
        for row in self.grid:
            for col in row:
                if col == Tile.RED:
                    print('#', end='')
                elif col == Tile.GREEN:
                    print('X', end='')
                else:
                    print('.', end='')
            print()

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    reds = [tuple([int(num) for num in line.strip().split(',')]) for line in inputfile]
    grid = CompactedGrid(reds)

    largest = 0
    for i in range(len(reds) - 1):
        a = reds[i]
        for j in range(i + 1, len(reds)):
            b = reds[j]
            size = (abs(a[0] - b[0])+1) * (abs(a[1] - b[1])+1)
            if size > largest: # This is a possible candidate to check
                if grid.check_box(a, b):
                    largest = size
    return largest

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
