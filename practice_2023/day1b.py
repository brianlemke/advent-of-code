#!/usr/bin/env python3

# https://adventofcode.com/2023/day/1

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2023_day1.txt')

def find_match(line, reverse=False):
    """Find the first number or digit that matches"""
    keys = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
    }

    for i, _ in enumerate(line):
        substr = line[-(i+1):] if reverse else line[i:]
        for text, digit in keys.items():
            if substr.startswith(digit) or substr.startswith(text):
                return digit

def calibrate(line):
    """Return the calibration value for a single line"""

    first = find_match(line, False)
    last = find_match(line, True)
    value = int(first + last)
    return value

def solve(inputfile):
    """Read the file and return a solution"""
    lines = [line.rstrip() for line in inputfile]
    calibrations = [calibrate(line) for line in lines]
    sum = functools.reduce(lambda a, b: a+b, calibrations)
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer = solve(open(args.inputfile))
    print(f'Answer: {answer}')