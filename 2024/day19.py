#!/usr/bin/env python3

# https://adventofcode.com/2024/day/19

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day19.txt')

def parse_input(inputfile):
    """Returns (towels, designs)"""
    lines = [line.strip() for line in inputfile]
    towels = [towel.strip() for towel in lines[0].split(',')]
    designs = [line.strip() for line in lines[2:]]
    return (towels, designs)

def is_design_possible(towels, design):
    if len(design) == 0: # Recursion end
        return True
    
    possible_starts = [towel for towel in towels if design.startswith(towel)]
    for start in possible_starts:
        if is_design_possible(towels, design[len(start):]):
            return True
        
    return False

TOWELS = []
@functools.cache
def count_arrangements(design):
    if len(design) == 0: # Recursion end
        return 1
    
    arrangements = 0
    possible_starts = [towel for towel in TOWELS if design.startswith(towel)]
    for start in possible_starts:
        arrangements += count_arrangements(design[len(start):])
        
    return arrangements

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    towels, designs = parse_input(inputfile)
    possible_designs = [True for design in designs if is_design_possible(towels, design)]
    return len(possible_designs)

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    global TOWELS
    TOWELS, designs = parse_input(inputfile)
    arrangements = 0
    for design in designs:
        count = count_arrangements(design)
        arrangements += count
    return arrangements

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
