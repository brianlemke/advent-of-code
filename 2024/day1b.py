#!/usr/bin/env python3

# https://adventofcode.com/2024/day/1

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day1.txt')

def occurrence_map(list):
    """Turn a list of numbers into a map of the number and
    how many times it appears in the list"""
    dict = {x: 0 for x in list}
    for e in list:
        dict[e] = dict[e] + 1
    return dict

def make_lists(lines):
    """Read the input lines into a zipped list"""
    a, b = [], []
    for line in lines:
        vals = [x for x in line.split(' ') if x != '']
        a.append(int(vals[0]))
        b.append(int(vals[1]))
    return a, b

def lookup_if_exists(key, table):
    """"""

def solve(inputfile):
    """Read the file and return a solution"""
    lines = [line.strip() for line in inputfile]
    left, right = make_lists(lines)
    lookup_table = occurrence_map(right)
    values = [x * lookup_table.get(x, 0) for x in left]
    sum = functools.reduce(lambda sum, v: sum + v, values, 0)
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer = solve(open(args.inputfile))
    print(f'Answer: {answer}')