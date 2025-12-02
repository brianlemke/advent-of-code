#!/usr/bin/env python3

# https://adventofcode.com/2024/day/1

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day1.txt')

class Solver:
    def __init__(self):
        self.position = 50
        self.zero_stop = 0
        self.zero_click = 0

    def turn_left(self, times):
        start_position = self.position
        self.position -= times
        if self.position <= 0 and start_position != 0:
            self.zero_click += 1
        if self.position < 0: # Recursive case when we pass zero
            self.position = 99
            self.turn_left(times - start_position - 1)
        elif self.position == 0:
            self.zero_stop += 1

    def turn_right(self, times):
        start_position = self.position
        self.position += times
        if self.position > 99:
            self.zero_click += 1
        if self.position > 99: # Recursive case when we pass 99
            self.position = 0
            self.turn_right(times - (99 - start_position) - 1)
        elif self.position == 0:
            self.zero_stop += 1

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    solver = Solver()
    for line in inputfile:
        times = int(line[1:])
        if line[0] == 'L':
            solver.turn_left(times)
        else:
            solver.turn_right(times)
    return solver.zero_stop

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    solver = Solver()
    for line in inputfile:
        times = int(line[1:])
        if line[0] == 'L':
            solver.turn_left(times)
        else:
            solver.turn_right(times)
    return solver.zero_click

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
