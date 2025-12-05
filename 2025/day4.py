#!/usr/bin/env python3

# https://adventofcode.com/2024/day/4

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day4.txt')

def is_paper(grid, row, col):
    if row < 0 or col < 0:
        return False
    if row >= len(grid):
        return False
    if col >= len(grid[row]):
        return False
    return grid[row][col]

def find_adjacencies(row, col) -> list[(int, int)]:
    return [ # Clockwise from top-left
        (row-1, col-1),
        (row-1, col),
        (row-1, col+1),
        (row, col+1),
        (row+1, col+1),
        (row+1, col),
        (row+1, col-1),
        (row, col-1),
    ]

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    count = 0
    grid: list[list[bool]] = [[True if col == '@' else False for col in row.strip()] for row in inputfile]
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if is_paper(grid, row, col):
                # Check all adjacent squares
                matches = list(filter(lambda point: is_paper(grid, point[0], point[1]), find_adjacencies(row, col)))
                if len(matches) < 4:
                    count += 1
    return count

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    count_removed = 0
    any_removed = True
    grid: list[list[bool]] = [[True if col == '@' else False for col in row.strip()] for row in inputfile]
    while any_removed:
        any_removed = False # Have to find a removal to loop the next time
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if is_paper(grid, row, col):
                    # Check all adjacent squares
                    matches = list(filter(lambda point: is_paper(grid, point[0], point[1]), find_adjacencies(row, col)))
                    if len(matches) < 4:
                        grid[row][col] = False
                        count_removed += 1
                        any_removed = True
    return count_removed

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
