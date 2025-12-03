#!/usr/bin/env python3

# https://adventofcode.com/2024/day/2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day2.txt')

def build_ranges(line) -> list[(int, int)]:
    ranges = []
    for range in line.split(','):
        parts = range.split('-')
        ranges.append((int(parts[0]), int(parts[1])))
    return ranges

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    sum = 0
    ranges = build_ranges(''.join(inputfile).strip())
    for r in ranges:
        for num in range(r[0], r[1] + 1):
            numstr = str(num)
            length = len(numstr)
            if length % 2 == 0:
                first = numstr[0:length//2]
                second = numstr[length//2:length]
                if first == second:
                    sum += num
    return sum

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    sum = 0
    ranges = build_ranges(''.join(inputfile).strip())
    for r in ranges:
        for num in range(r[0], r[1] + 1):
            numstr = str(num)
            length = len(numstr)
            mid = length // 2 # Can't have a repeated substring longer than half
            # Check every possible start string of up to the mid length
            found = False
            for sublength in range(1, mid + 1):
                if found:
                    break
                sub = numstr[0:sublength]
                # Repeat that substring in multiple variations to see if it matches
                times = 1
                while True:
                    mul = sub * times
                    times += 1
                    if len(mul) > length: # termination case, stop repeating now that it is too long
                        break
                    elif len(mul) == length and mul == numstr:
                        found = True
                        sum += num
                        break
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
