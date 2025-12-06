#!/usr/bin/env python3

# https://adventofcode.com/2024/day/5

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day5.txt')

class Input:
    def __init__(self, inputfile):
        self.ranges:list[list[int]] = []
        self.ingredients: list[int] = []

        second_half = False
        for line in inputfile:
            if not line.strip():
                second_half = True
            elif second_half:
                self.ingredients.append(int(line))
            else:
                self.ranges.append([int(c) for c in line.strip().split('-')])

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    input = Input(inputfile)
    sum = 0
    for i in input.ingredients:
        for r in input.ranges:
            if i >= r[0] and i <= r[1]:
                # This ingredient is fresh
                sum += 1
                break
    return sum

def add_new_ranges(processed_ranges, new_range):
    """Split up the new range into multiple sub-ranges that aren't already processed"""
    for range in processed_ranges:
        if new_range[0] > new_range[1]:
            # We have fully eliminated this range at some point in the process, we're done
            break
        
        # Check if there is an overlap
        if new_range[0] <= range[1] and new_range[1] >= range[0]:
            # Intersection, truncate to smaller range(s)
            if new_range[0] < range[0] and new_range[1] > range[1]:
                # Full overlap, split into two smaller subranges and add them
                first = (new_range[0], range[0] - 1)
                second = (range[1] + 1, new_range[1])
                add_new_ranges(processed_ranges, first)
                add_new_ranges(processed_ranges, second)
                return
            elif new_range[0] >= range[0]:
                # Start is fully contained, just truncate to end
                new_range[0] = range[1] + 1
            elif new_range[1] <= range[1]:
                # End is fully contained, truncate to start
                new_range[1] = range[0] - 1

    # We've gotten this far without having to split up the range, so add it
    if new_range[0] <= new_range[1]:
        processed_ranges.append(new_range)

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    input = Input(inputfile)
    processed_ranges: list[(int, int)] = []
    for range in input.ranges:
        # Only add the portions of the range to processed_ranges that aren't already covered
        add_new_ranges(processed_ranges, range)

    # Sum everything up
    sum = 0
    for range in processed_ranges:
        sum += range[1] - range[0] + 1
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
