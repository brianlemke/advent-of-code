#!/usr/bin/env python3

# https://adventofcode.com/2024/day/6

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day6.txt')

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    problems: list[list[int]] = []
    grand_total = 0
    for line in inputfile:
        columns = [c.strip() for c in line.split()]
        plus = columns[0].strip() == '+'
        times = columns[0].strip() == '*'
        if columns[0] in ['+', '*']:
            # Solve the problems
            for i, op in enumerate(columns):
                if op == '+':
                    solution = functools.reduce(lambda a,b: a+b, problems[i], 0)
                else:
                    solution = functools.reduce(lambda a,b: a*b, problems[i], 1)
                grand_total += solution
        else:
            if len(problems) == 0: # initialize the problems
                problems = [[] for _ in columns]
            for i, c in enumerate(columns):
                problems[i].append(int(c))
    return grand_total

class Problem:
    operands: list[str]
    operator: str
    column_width: int

    def __init__(self, operator):
        self.operator = operator
        self.column_width = 1
        self.operands = []

    def solve_colunmnwise(self):
        # Look vertically down each operand to build a new set of operands
        fixed_operands: list[str] = []
        for i in range(self.column_width):
            rearranged = ''.join([op[i] for op in self.operands])
            if rearranged.strip():
                fixed_operands.append(int(rearranged))
        if self.operator == '+':
            solution = functools.reduce(lambda a,b: a+b, fixed_operands, 0)
        else:
            solution = functools.reduce(lambda a,b: a*b, fixed_operands, 1)
        return solution

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    problems:list[Problem] = []
    lines = [line for line in inputfile]

    # The operators are always at the start of the line, so use the spacing to determine the column width
    operators = lines[-1].strip('\n')
    for ch in operators:
        if ch in ['+', '*']:
            problems.append(Problem(ch))
        else:
            problems[-1].column_width += 1
    
    # Iterate over each line, and break on the columns while preserving whitespace within the columns
    for line in lines[:-1]:
        i = 0
        for problem in problems:
            next_i = i + problem.column_width
            problem.operands.append(line[i:next_i])
            i = next_i
    
    grand_total = 0
    for p in problems:
        grand_total += p.solve_colunmnwise()
    return grand_total

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
