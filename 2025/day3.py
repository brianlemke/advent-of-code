#!/usr/bin/env python3

# https://adventofcode.com/2024/day/3

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day3.txt')

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    sum = 0
    for line in inputfile:
        bank = [int(b) for b in list(line.strip())]
        max_joltage = 0
        # Try every possible pair of batteries
        for i in range(0, len(bank) - 1):
            for j in range(i+1, len(bank)):
                joltage = bank[i]*10 + bank[j]
                max_joltage = max(max_joltage, joltage)
        sum += max_joltage
    return sum

@functools.cache
def pick_batteries(bank: str, count:int) -> str:
    if count == 0 or len(bank) < count:
        return ''
    max_joltage = 0
    for i in range(0, len(bank) - count + 1):
        joltage = bank[i] + pick_batteries(bank[i+1:], count-1)
        max_joltage = max(max_joltage, int(joltage))
    return str(max_joltage)

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    sum = 0
    for line in inputfile:
        max_joltage = pick_batteries(line.strip(), 12)
        sum += int(max_joltage)
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
