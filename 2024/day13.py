#!/usr/bin/env python3

# https://adventofcode.com/2024/day/13

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day13.txt')

class Machine():
    def __init__(self, lines):
        button_re = r'Button .: X\+(\d+), Y\+(\d+)'
        match_a = re.search(button_re, lines[0])
        match_b = re.search(button_re, lines[1])
        match_prize = re.search(r'.*X=(\d+), Y=(\d+)', lines[2])

        self.a = (int(match_a[1]), int(match_a[2]))
        self.b = (int(match_b[1]), int(match_b[2]))
        self.prize = (int(match_prize[1]), int(match_prize[2]))

def parse_machines(inputfile):
    """Get a list of machines, each an object like:
    {
        a: (x,y)
        b: (x,y)
        prize: (x,y)
    }"""
    machines = []
    lines = [l.strip() for l in inputfile]
    for start in range(0, len(lines), 4):
        machines.append(Machine(lines[start:start+4]))
    return machines

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    machines = parse_machines(inputfile)
    tokens = 0
    for machine in machines:
        best_tokens = None
        for an in range(0, 100):
            dx = machine.prize[0] - an * machine.a[0]
            dy = machine.prize[1] - an * machine.a[1]
            if dx < 0 or dy < 0:
                continue # Overshot with just one button
            elif dx % machine.b[0] != 0 or dy % machine.b[1] != 0:
                continue # Cannot divide the remaining distance with button b
            else:
                bn = int(dx / machine.b[0]) # Times to push button to meet x distance
                if bn * machine.b[1] == dy:
                    # Also meets y distance, valid combination
                    cur_tokens = an*3 + bn*1
                    if best_tokens is None or cur_tokens < best_tokens:
                        best_tokens = cur_tokens
        if best_tokens is not None:
            tokens += best_tokens
    return tokens

def solve_b(inputfile, additional=10000000000000):
    """Read the file and return a solution for Part Two"""
    machines = parse_machines(inputfile)
    sum_tokens = 0
    for machine in machines:
        machine.prize = (machine.prize[0]+additional, machine.prize[1]+additional)

        b_pushes_numerator = machine.a[0]*machine.prize[1] - machine.a[1]*machine.prize[0]
        b_pushes_denominator = machine.a[0]*machine.b[1] - machine.a[1]*machine.b[0]
        if b_pushes_denominator != 0:
            b_pushes = b_pushes_numerator / b_pushes_denominator
            if b_pushes.is_integer():
                a_pushes = (machine.prize[0] - b_pushes*machine.b[0]) / machine.a[0]
                if a_pushes.is_integer():
                    # We have a solution!
                    tokens = int(a_pushes)*3 + int(b_pushes)*1
                    sum_tokens += tokens
    return sum_tokens

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
