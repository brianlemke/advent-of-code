#!/usr/bin/env python3

# https://adventofcode.com/2024/day/8

import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day8.txt')

class Antenna:
    def __init__(self, type, row, col):
        self.type = type
        self.row = row
        self.col = col
    
    def coords(self):
        return (self.row, self.col)
    
MAX_COL = 0
MAX_ROW = 0

def in_bounds(row, col):
    return row >=0 and row <= MAX_ROW and col >= 0 and col <= MAX_COL
    
def group_antennae_by_type(inputfile):
    global MAX_COL, MAX_ROW

    antennae = []
    for row, line in enumerate(inputfile):
        MAX_ROW = max(row, MAX_ROW)
        for col, val in enumerate(line.strip()):
            MAX_COL = max(col, MAX_COL)
            if val != '.':
                antennae.append(Antenna(val, row, col))

    # Group by type
    antennae = sorted(antennae, key=lambda a: a.type)
    types = itertools.groupby(antennae, key=lambda a: a.type)
    return types

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    antinodes = {}
    def add_antinode(type, row, col):
        if in_bounds(row, col):
            if (row, col) in antinodes:
                antinodes[(row,col)].append(type)
            else:
                antinodes[(row,col)] = [type]

    for key, group in group_antennae_by_type(inputfile):
        # Find all combinations of any two antennae in this group
        for combo in itertools.combinations(group, 2):
            # Calculate the first antinode
            r1 = combo[0].row - (combo[1].row - combo[0].row)
            c1 = combo[0].col - (combo[1].col - combo[0].col)
            add_antinode(key, r1, c1)
            # Calculate the second antinode
            r2 = combo[1].row - (combo[0].row - combo[1].row)
            c2 = combo[1].col - (combo[0].col - combo[1].col)
            add_antinode(key, r2, c2)

    return len(antinodes.keys())

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    antinodes = {}
    def add_antinode(type, row, col):
        if in_bounds(row, col):
            if (row, col) in antinodes:
                antinodes[(row,col)].append(type)
            else:
                antinodes[(row,col)] = [type]
    
    for key, group in group_antennae_by_type(inputfile):
        # Find all combinations of any two antennae in this group
        for combo in itertools.combinations(group, 2):
            row_diff = combo[1].row - combo[0].row
            col_diff = combo[1].col - combo[0].col
            # Find all combos starting from the first antenna until we run off
            row,col = combo[0].row, combo[0].col
            while in_bounds(row, col):
                add_antinode(key, row, col)
                row += row_diff
                col += col_diff
            # Find all combos starting from the second antenna until we run off
            row,col = combo[1].row, combo[1].col
            while in_bounds(row, col):
                add_antinode(key, row, col)
                row -= row_diff
                col -= col_diff

    return len(antinodes.keys())

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
