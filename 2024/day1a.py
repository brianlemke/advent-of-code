#!/usr/bin/env python3

# https://adventofcode.com/2024/day/1

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day1.txt')

def zip_input_lines(lines):
    """Read the input lines into a zipped list"""
    a, b = [], []
    for line in lines:
        vals = [x for x in line.split(' ') if x != '']
        a.append(int(vals[0]))
        b.append(int(vals[1]))
    return zip(sorted(a), sorted(b))

def solve(inputfile):
    """Read the file and return a solution"""
    lines = [line.strip() for line in inputfile]
    matches = zip_input_lines(lines)
    sum = functools.reduce(lambda sum, t: sum + abs(t[0]-t[1]), matches, 0)
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer = solve(open(args.inputfile))
    print(f'Answer: {answer}')