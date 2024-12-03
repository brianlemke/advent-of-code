#!/usr/bin/env python3

# https://adventofcode.com/2024/day/2

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day2.txt')

def differences(list):
    results = []
    for i in range(1, len(list)):
        results.append(list[i] - list[i-1])
    return results

def valid_report(report):
    diffs = differences(report)
    # Check if monotonically changing
    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
         # Check in bounds
         if all(abs(d) >= 1 and abs(d) <= 3 for d in diffs):
              return True
    return False

def permute_report(report):
    """Generate permutations of the report as-is, or with any single item removed"""
    permutations = [report]
    for i in range(0, len(report)):
        copy = report.copy()
        del copy[i]
        permutations.append(copy)
    return permutations

def solve_a(inputfile):
    """Read the file and return a solution"""
    reports = parse_reports(inputfile)
    valid_reports = 0
    for report in reports:
        if valid_report(report):
            valid_reports = valid_reports + 1
    return valid_reports

def solve_b(inputfile):
    """Read the file and return a solution"""
    reports = parse_reports(inputfile)
    valid_reports = 0
    for report in reports:
        permutations = permute_report(report)
        if any(valid_report(p) for p in permutations):
            valid_reports = valid_reports + 1
    return valid_reports

def parse_reports(inputfile):
    reports = [[int(y) for y in x.strip().split()] for x in inputfile]

    return reports

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
