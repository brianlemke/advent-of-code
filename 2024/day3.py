#!/usr/bin/env python3

# https://adventofcode.com/2024/day/3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day3.txt')

def solve_a(input):
    """Read the file and return a solution"""
    matches = re.findall(r'mul\((\d+),(\d+)\)', input)
    sum = 0
    for match in matches:
        sum = sum + (int(match[0]) * int(match[1]))
    return sum

def solve_b(input):
    """Read the file and return a solution"""
    matches = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', input)
    sum = 0
    enabled = True
    for match in matches:
        if match == 'do()':
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            digits = re.match(r'mul\((\d+),(\d+)\)', match)
            sum = sum + (int(digits.group(1)) * int(digits.group(2)))
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile).read())
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile).read())
    print(f'Answer (part B): {answer_b}')
