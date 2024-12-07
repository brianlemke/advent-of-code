#!/usr/bin/env python3

# https://adventofcode.com/2024/day/4

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day4.txt')

def safe_match(coordinate, letter, matrix):
    """Check whether the designated location is a specific letter, returning False
    if the location is out-of-bounds"""
    (row, col) = coordinate
    if row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix):
        return matrix[row][col] == letter
    else:
        return False

def is_cross_center(row, col, matrix):
    """Determine if this point is the center of a MAS cross"""
    # Can only be a cross if this point is an A
    if matrix[row][col] == 'A':
        # All surrounding coordinates must be in bounds
        if row - 1 >= 0 and col - 1 >= 0 and row + 1 < len(matrix) and col + 1 < len(matrix):
            top_left = matrix[row-1][col-1]
            top_right = matrix[row-1][col+1]
            bottom_left = matrix[row+1][col-1]
            bottom_right = matrix[row+1][col+1]
            # Check if the top-left to bottom-right diagonal is valid
            if top_left == 'M' and bottom_right == 'S' or top_left == 'S' and bottom_right == 'M':
                # Check if the top-right to bottom-left diagonal is valid
                if top_right == 'M' and bottom_left == 'S' or top_right == 'S' and bottom_left == 'M':
                    return True
    return False

def count_point(row, col, matrix):
    """Find how many 'XMAS' entries this point is the start of in all directions"""

    candidates = []
    candidates.append([(row, col + i) for i in range(0, 4)])     # Go right 4 spaces
    candidates.append([(row, col - i) for i in range(0, 4)])     # Go left 4 spaces
    candidates.append([(row - i, col) for i in range(0, 4)])     # Go up 4 spaces
    candidates.append([(row + i, col) for i in range(0, 4)])     # Go down 4 spaces
    candidates.append([(row - i, col - i) for i in range(0, 4)]) # Go diagonally up-left 4 spaces
    candidates.append([(row - i, col + i) for i in range(0, 4)]) # Go diagonally down-left 4 spaces
    candidates.append([(row + i, col - i) for i in range(0, 4)]) # Go diagonally up-right 4 spaces
    candidates.append([(row + i, col + i) for i in range(0, 4)]) # Go diagonally down-right 4 spaces

    matches = 0
    for candidate in candidates:
        if safe_match(candidate[0], 'X', matrix):
            if safe_match(candidate[1], 'M', matrix):
                if safe_match(candidate[2], 'A', matrix):
                    if safe_match(candidate[3], 'S', matrix):
                        matches += 1
    return matches

def solve_a(inputfile):
    """Read the file and return a solution"""
    rows = [l.rstrip() for l in inputfile]
    sum = 0
    for row in range(0, len(rows)):
        for col in range(0, len(rows)):
            sum += count_point(row, col, rows)
    return sum

def solve_b(inputfile):
    """Read the file and return a solution"""
    rows = [l.rstrip() for l in inputfile]
    sum = 0
    for row in range(0, len(rows)):
        for col in range(0, len(rows)):
            if is_cross_center(row, col, rows):
                sum += 1
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
