#!/usr/bin/env python3

# https://adventofcode.com/2024/day/7

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day7.txt')

def is_valid_equation(result, inputs, start=None, concatenate=False):
    """Can this result be achieved by compining the inputs with operators, runs recursively"""
    if start is None:
        start = inputs[0]
        inputs = inputs[1:]
    
    if len(inputs) == 0:
        return result == start
    
    # Recurse with both additive and multiplicative
    next = inputs[0]
    inputs = inputs[1:]
    if concatenate:
        return is_valid_equation(result, inputs, start + next, concatenate) \
            or is_valid_equation(result, inputs, start * next, concatenate) \
            or is_valid_equation(result, inputs, int(f"{start}{next}"), concatenate)
    else:
        return is_valid_equation(result, inputs, start + next) or is_valid_equation(result, inputs, start * next)

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    equations = [line.strip() for line in inputfile]
    sum = 0
    for equation in equations:
        result = int(equation.split(':')[0].strip())
        inputs = [int(x) for x in equation.split(':')[1].strip().split()]
        if is_valid_equation(result, inputs):
            sum += result
    return sum

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    equations = [line.strip() for line in inputfile]
    sum = 0
    for equation in equations:
        result = int(equation.split(':')[0].strip())
        inputs = [int(x) for x in equation.split(':')[1].strip().split()]
        if is_valid_equation(result, inputs, concatenate=True):
            sum += result
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
