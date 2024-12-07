#!/usr/bin/env python3

# https://adventofcode.com/2024/day/x

import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day5.txt')

def parse_file(inputfile):
    """Convert the file into a list of instructions and a list of updates"""
    lines = [l.strip() for l in inputfile]

    # Split the lines into instructions and update sections
    sections = [list(y) for x, y in itertools.groupby(lines, lambda z: len(z) == 0 or z.isspace()) if not x]
    instructions = sections[0]
    updates = sections[1]

    # Turn each line into a list, converted to ints
    instructions = [[int(v) for v in i.split('|')] for i in instructions]
    updates = [[int(p) for p in u.split(',')] for u in updates]

    return (instructions, updates)

def is_valid_update(instructions, update):
    """Check if the update line passes all instructions"""

    # Filter instructions to only those that apply to this update
    instructions = [i for i in instructions if i[0] in update and i[1] in update]
    for index, page in enumerate(update):
        # Find all instructions where another page must be after this one
        for required in [i[1] for i in instructions if i[0] == page]:
            # Make sure all of these required pages are later in the update
            if required not in update[index+1:]:
                return False
    return True

def fix_update(instructions, update):
    """Re-order an update to match the instructions"""

    # Filter instructions to only those that apply to this update
    instructions = [i for i in instructions if i[0] in update and i[1] in update]

    fixed_update = []
    def can_print(page):
        """Check if the page can be printed given the already-printed pages"""
        for required in [i[0] for i in instructions if i[1] == page]:
            if required not in fixed_update:
                return False
        return True

    while len(update) > 0:
        # Find the next page to add that doesn't violate any constraints
        for index, page in enumerate(update):
            if can_print(page):
                fixed_update.append(page)
                del update[index]
                break

    return fixed_update

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    # Find the empty line to split the input into instruction lined and update lines
    instructions, updates = parse_file(inputfile)

    sum = 0
    for update in updates:
        if is_valid_update(instructions, update):
            # Find the middle number
            middle = int(len(update) / 2)
            sum += update[middle]
    return sum

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    # Find the empty line to split the input into instruction lined and update lines
    instructions, updates = parse_file(inputfile)

    sum = 0
    for update in updates:
        if not is_valid_update(instructions, update):
            fixed_update = fix_update(instructions, update)
            # Find the middle number
            middle = int(len(fixed_update) / 2)
            sum += fixed_update[middle]
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
