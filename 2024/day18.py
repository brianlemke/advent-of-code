#!/usr/bin/env python3

# https://adventofcode.com/2024/day/18

import argparse
from queue import Queue

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day18.txt')

def shortest_path(grid):
    """Run a BFS to find the shortest path going only through False segments"""
    height, width = len(grid), len(grid[0])
    q = Queue()       # to navigate
    visited = set()   # visited
    q.put((0,0,0))    # (x,y,cost)
    visited.add((0,0))
    while not q.empty():
        size = q.qsize()
        (x, y, cost) = q.get()
        # Identify the valid neighbors
        neighbors = [(x-1,y,cost+1), (x,y-1,cost+1), (x+1,y,cost+1), (x,y+1,cost+1)]
        is_in_bounds = lambda n: n[0] >= 0 and n[0] < width and n[1] >=0 and n[1] < height
        is_corrupted = lambda n: grid[n[1]][n[0]]
        is_visited = lambda n: (n[0],n[1]) in visited
        valid_neighbors = [n for n in neighbors if is_in_bounds(n) and not is_corrupted(n) and not is_visited(n)]
        for n in valid_neighbors:
            if n[0] == width-1 and n[1] == height-1:
                return n[2] # Found the exit
            q.put(n)
            visited.add((n[0],n[1]))
    return None

def solve_a(inputfile, size=71, bytes=1024):
    """Read the file and return a solution for Part One"""
    grid = [[False for y in range(0, size)] for x in range(0, size)]

    # Calculate corrupted areas
    for i, line in enumerate(inputfile):
        if i >= bytes:
            break
        values = line.strip().split(',')
        x = int(values[0])
        y = int(values[1])
        grid[y][x] = True # Corrupted

    # Now run a BFS to find the shortest path
    return shortest_path(grid)

def solve_b(inputfile, size=71, bytes=1024):
    """Read the file and return a solution for Part Two"""
    grid = [[False for y in range(0, size)] for x in range(0, size)]

    for i, line in enumerate(inputfile):
        values = line.strip().split(',')
        x = int(values[0])
        y = int(values[1])
        grid[y][x] = True # Corrupted

        if i < bytes:
            # Still filling out corrupted areas
            continue

        # Check if there is a path to the exit
        length = shortest_path(grid)
        if length is None:
            return f'{x},{y}'

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
