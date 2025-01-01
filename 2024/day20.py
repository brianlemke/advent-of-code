#!/usr/bin/env python3

# https://adventofcode.com/2024/day/20

import argparse
from queue import Queue
from enum import Enum
from utilities import print_progress_bar

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day20.txt')

class Item(Enum):
    Empty = '.'
    Start = 'S'
    End = 'E'
    Wall = '#'

class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def parse_input(inputfile):
    """Returns (grid, start, end)"""
    grid = [[Item(ch) for ch in row.strip()] for row in inputfile]
    start = None
    end = None
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item == Item.Start:
                start = Point(y, x)
            elif item == Item.End:
                end = Point(y, x)
    return (grid, start, end)

def best_time(grid, start_point, end_point, cheat=None):
    """Run a BFS to find the shortest path going only through False segments"""
    height, width = len(grid), len(grid[0])
    q = Queue()       # to navigate
    visited = set()   # visited
    q.put((start_point.col,start_point.row,0))    # (x,y,cost)
    visited.add((start_point.col,start_point.row))
    while not q.empty():
        (x, y, cost) = q.get()
        # Identify the valid neighbors
        neighbors = [(x-1,y,cost+1), (x,y-1,cost+1), (x+1,y,cost+1), (x,y+1,cost+1)]
        is_in_bounds = lambda n: n[0] >= 0 and n[0] < width and n[1] >=0 and n[1] < height
        is_wall = lambda n: grid[n[1]][n[0]] == Item.Wall
        is_cheat = lambda n: cheat is not None and cheat[2].row == n[1] and cheat[2].col == n[0] and cheat[0].row == y and cheat[0].col == x
        is_visited = lambda n: (n[0],n[1]) in visited
        valid_neighbors = [n for n in neighbors if is_in_bounds(n) and (not is_wall(n) or is_cheat(n)) and not is_visited(n)]
        for n in valid_neighbors:
            if n[0] == end_point.col and n[1] == end_point.row:
                return n[2] # Found the exit
            q.put(n)
            visited.add((n[0],n[1]))
    return None

def solve_a(inputfile, timesave=100):
    """Read the file and return a solution for Part One"""
    grid, start, end = parse_input(inputfile)
    non_cheated_time = best_time(grid, start, end)

    height, width = len(grid), len(grid[0])
    in_bounds = lambda p: p.row >= 0 and p.row < height and p.col >= 0 and p.col < width
    is_visitable = lambda p: grid[p.row][p.col] != Item.Wall

    # Identify all possible cheats (start_point,end_point,skipped_wall)
    cheats = []
    for row, line in enumerate(grid):
        for col, item in enumerate(line):
            if item == Item.Wall:
                wall = Point(row, col)
                left = Point(row, col-1)
                right = Point(row, col+1)
                up = Point(row-1, col)
                down = Point(row+1, col)

                # Check if the up-down cheat is possible
                if in_bounds(up) and is_visitable(up) and in_bounds(down) and is_visitable(down):
                    cheats.append((up, down, wall))
                    cheats.append((down, up, wall))
                
                # Check if the left-right cheat is possible
                if in_bounds(left) and is_visitable(left) and in_bounds(right) and is_visitable(right):
                    cheats.append((left, right, wall))
                    cheats.append((right, left, wall))
    
    count = 0
    total_count = len(cheats)
    for progress, cheat in enumerate(cheats):
        print_progress_bar(progress, total_count-1)
        time = best_time(grid, start, end, cheat)
        diff = non_cheated_time - time
        if diff >= timesave:
            count += 1

    return count

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    return None

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
