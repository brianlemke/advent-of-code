#!/usr/bin/env python3

# https://adventofcode.com/2023/day/1

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2023_day1.txt')

def calibrate(line):
    """Return the calibration value for a single line"""
    # Keep only digits
    digits = [c for c in line if c.isdigit()]
    return int(digits[0] + digits[-1])

def solve(inputfile):
    """Read the file and return a solution"""
    lines = [line.rstrip() for line in open(inputfile)]
    calibrations = [calibrate(line) for line in lines]
    sum = functools.reduce(lambda a, b: a+b, calibrations)
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer = solve(args.inputfile)
    print(f'Answer: {answer}')