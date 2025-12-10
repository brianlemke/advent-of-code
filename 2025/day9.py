#!/usr/bin/env python3

# https://adventofcode.com/2024/day/9

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day9.txt')

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    reds = [tuple([int(num) for num in line.strip().split(',')]) for line in inputfile]
    largest = 0
    for i in range(len(reds) - 1):
        a = reds[i]
        for j in range(i + 1, len(reds)):
            b = reds[j]
            size = (abs(a[0] - b[0])+1) * (abs(a[1] - b[1])+1)
            if size > largest:
                largest = size
    return largest

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    return None

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
