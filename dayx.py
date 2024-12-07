#!/usr/bin/env python3

# https://adventofcode.com/2024/day/x

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_dayx.txt')

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    return None

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    return None

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
