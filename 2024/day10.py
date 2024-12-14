#!/usr/bin/env python3

# https://adventofcode.com/2024/day/10

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day10.txt')

def parse_map(inputfile):
    map = [[int(c) for c in l.strip()] for l in inputfile]
    return map # [row][col]    

def trailhead_score(map, row, col):
    height = len(map)
    width = len(map[0])

    terminuses = set() # (row, col)

    # Recursive function
    def trailhead_score_helper(cr, cc):
        if map[cr][cc] == 9:
            terminuses.add((cr, cc))
            return
        
        next = [(cr-1,cc), (cr,cc+1), (cr+1,cc), (cr,cc-1)]
        for nr, nc in next:
            if nr < 0 or nr >= height or nc < 0 or nc >= width:
                pass # out of bounds
            elif map[nr][nc] == map[cr][cc] + 1:
                trailhead_score_helper(nr, nc)
            else:
                pass # not a valid trail
    
    trailhead_score_helper(row, col)

    return len(terminuses)

def trailhead_rating(map, row, col):
    height = len(map)
    width = len(map[0])

    # Recursive function
    def trailhead_rating_helper(cr, cc):
        if map[cr][cc] == 9:
            return 1
        
        rating = 0
        next = [(cr-1,cc), (cr,cc+1), (cr+1,cc), (cr,cc-1)]
        for nr, nc in next:
            if nr < 0 or nr >= height or nc < 0 or nc >= width:
                pass # out of bounds
            elif map[nr][nc] == map[cr][cc] + 1:
                rating += trailhead_rating_helper(nr, nc)
            else:
                pass # not a valid trail
        return rating
    
    return trailhead_rating_helper(row, col)

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    map = parse_map(inputfile)

    sum = 0
    for row, line in enumerate(map):
        for col, _ in enumerate(line):
            if map[row][col] == 0:
                sum += trailhead_score(map, row, col)
    return sum

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    map = parse_map(inputfile)

    sum = 0
    for row, line in enumerate(map):
        for col, _ in enumerate(line):
            if map[row][col] == 0:
                sum += trailhead_rating(map, row, col)
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
