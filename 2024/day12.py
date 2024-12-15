#!/usr/bin/env python3

# https://adventofcode.com/2024/day/12

import argparse
from enum import Enum

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day12.txt')

ROWS = 0
COLS = 0
def parse_grid(inputfile):
    global ROWS, COLS
    grid = [[col for col in row.strip()] for row in inputfile]
    ROWS = len(grid)
    COLS = len(grid[0])
    return grid

def compute_region_a(grid, row, col, handled):
    handled.add((row, col))

    area = 1 # For this cell we are processing now
    perimeter = 0
    height = len(grid)
    width = len(grid[0])

    adjacent = [(row-1,col), (row,col+1), (row+1,col), (row,col-1)]
    for r, c in adjacent:
        if r < 0 or r >= height or c < 0 or c >= width:
            perimeter += 1 # This is an edge
        else:
            is_handled = (r, c) in handled
            same_type = grid[row][col] == grid[r][c]
            if same_type:
                if not is_handled:
                    (a,p) = compute_region_a(grid, r, c, handled)
                    area += a
                    perimeter += p
            else:
                perimeter += 1
    return (area, perimeter)

def identify_region(grid, row, col, region):
    region.add((row,col))
    height = len(grid)
    width = len(grid[0])

    adjacent = [(row-1,col), (row,col+1), (row+1,col), (row,col-1)]
    for r, c in adjacent:
        if r < 0 or r >= height or c < 0 or c >= width:
            pass
        elif grid[r][c] == grid[row][col]:
            if (r,c) not in region:
                identify_region(grid, r, c, region)

    return region

class Side(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

def has_edge(region, row, col, side):
    match side:
        case Side.TOP:
            next = (row-1,col)
        case Side.RIGHT:
            next = (row,col+1)
        case Side.BOTTOM:
            next = (row+1,col)
        case Side.LEFT:
            next = (row,col-1)
    
    return next not in region

def build_edge(region, row, col, side, handled):
    handled.add((row,col))

    if side == Side.TOP or side == Side.BOTTOM:
        adjacent = [(row,col-1), (row,col+1)]
    else:
        adjacent = [(row-1,col), (row+1,col)]
    
    for point in adjacent:
        if point in region and point not in handled and has_edge(region, point[0], point[1], side):
            build_edge(region, point[0], point[1], side, handled)

def count_edges(region, side=None):
    if side == None:
        return count_edges(region, Side.TOP) + \
               count_edges(region, Side.RIGHT) + \
               count_edges(region, Side.BOTTOM) + \
               count_edges(region, Side.LEFT)
    
    edges = 0
    handled = set()
    for (row, col) in region:
        point = (row, col)
        if point not in handled:
            if has_edge(region, row, col, side):
                edges += 1
                build_edge(region, row, col, side, handled)
            else:
                handled.add(point)
    return edges

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    grid = parse_grid(inputfile)
    handled = set() # (row, col) already processed into a region
    fencing = 0
    for row, items in enumerate(grid):
        for col, _ in enumerate(items):
            if (row, col) not in handled:
                (a, p) = compute_region_a(grid, row, col, handled)
                fencing += a * p
    return fencing

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    grid = parse_grid(inputfile)
    regions = [] # Sets of (row, col) for each region
    for row, items in enumerate(grid):
        for col, _ in enumerate(items):
            if not any([(row,col) in region for region in regions]):
                region = set()
                identify_region(grid, row, col, region)
                regions.append(region)

    fencing = 0
    for region in regions:
        area = len(region)
        edges = count_edges(region)
        fencing += area * edges
    return fencing

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
