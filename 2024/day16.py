#!/usr/bin/env python3

# https://adventofcode.com/2024/day/16

import argparse
import heapq
from enum import Enum

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day16.txt')

class Item(Enum):
    Empty = '.'
    Wall = '#'
    Start = 'S'
    End = 'E'

class Direction(Enum):
    Left = '<'
    Up = '^'
    Right = '>'
    Down = 'v'

class Node:
    def __init__(self, x, y, direction, score=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.score = score
        self.previous = set()
    
    def __eq__(self, other):
        return self.x == other.x and \
            self.y == other.y and \
            self.direction == other.direction
    
    def __lt__(self, other):
        if self.score is None:
            return False
        elif other.score is None:
            return True
        else:
            return self.score < other.score
        
    def __hash__(self):
        return hash(self.key())
        
    def key(self):
        return (self.x, self.y, self.direction)

def parse_input(inputfile):
    grid = [[Item(ch) for ch in line.strip()] for line in inputfile]
    return grid

def find_neighbor_nodes(grid, node):
    """Find the valid neighbors with score"""
    height = len(grid)
    width = len(grid[0])

    neighbors = []
    # Can we move forward?
    nx, ny = node.x, node.y
    match node.direction:
        case Direction.Left:
            nx -= 1
        case Direction.Up:
            ny -= 1
        case Direction.Right:
            nx += 1
        case Direction.Down:
            ny += 1
    if nx >= 0 and nx < width and ny >= 0 and ny < height:
        if grid[ny][nx] != Item.Wall:
            # This is a valid move
            neighbors.append(Node(nx, ny, node.direction, node.score + 1))
    if node.direction == Direction.Up or node.direction == Direction.Down:
        neighbors.append(Node(node.x, node.y, Direction.Left, node.score + 1000))
        neighbors.append(Node(node.x, node.y, Direction.Right, node.score + 1000))
    else:
        neighbors.append(Node(node.x, node.y, Direction.Up, node.score + 1000))
        neighbors.append(Node(node.x, node.y, Direction.Down, node.score + 1000))
    return neighbors

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    grid = parse_input(inputfile)

    # Build a heap of all possible nodes
    nodes = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == Item.Start:
                nodes.append(Node(x, y, Direction.Left))
                nodes.append(Node(x, y, Direction.Up))
                nodes.append(Node(x, y, Direction.Right, 0)) # Initialize start score
                nodes.append(Node(x, y, Direction.Down))
            elif val != Item.Wall:
                nodes.append(Node(x, y, Direction.Left))
                nodes.append(Node(x, y, Direction.Up))
                nodes.append(Node(x, y, Direction.Right))
                nodes.append(Node(x, y, Direction.Down))

    # Dijkstra's algorithm
    unvisited = set(nodes.copy())
    nodes = dict([(node.key(), node) for node in nodes])

    while len(unvisited) > 0:
        next = min(unvisited)
        unvisited.remove(next)
        if next.score is None:
            break # Out of reachable nodes

        # Find neighbors and update their scores
        neighbors = find_neighbor_nodes(grid, next)
        for neighbor in neighbors:
            cached = nodes[neighbor.key()]
            if neighbor < cached:
                cached.score = neighbor.score
        
    # Find all the nodes that match the end state
    end_nodes = [t[1] for t in nodes.items() if grid[t[1].y][t[1].x] == Item.End]
    min_end = min(end_nodes)
    return min_end.score

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    grid = parse_input(inputfile)

    # Build a heap of all possible nodes
    nodes = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == Item.Start:
                nodes.append(Node(x, y, Direction.Left))
                nodes.append(Node(x, y, Direction.Up))
                nodes.append(Node(x, y, Direction.Right, 0)) # Initialize start score
                nodes.append(Node(x, y, Direction.Down))
            elif val != Item.Wall:
                nodes.append(Node(x, y, Direction.Left))
                nodes.append(Node(x, y, Direction.Up))
                nodes.append(Node(x, y, Direction.Right))
                nodes.append(Node(x, y, Direction.Down))

    # Dijkstra's algorithm
    unvisited = set(nodes.copy())
    nodes = dict([(node.key(), node) for node in nodes])

    while len(unvisited) > 0:
        next = min(unvisited)
        unvisited.remove(next)
        if next.score is None:
            break # Out of reachable nodes

        # Find neighbors and update their scores
        neighbors = find_neighbor_nodes(grid, next)
        for neighbor in neighbors:
            cached = nodes[neighbor.key()]
            if neighbor < cached:
                cached.score = neighbor.score
                cached.previous = set([next])
            elif neighbor.score == cached.score:
                cached.previous.add(next)

    # Walk backwards through all best paths and identify (x,y) seats
    good_seats = set()
    end_nodes = [t[1] for t in nodes.items() if grid[t[1].y][t[1].x] == Item.End]

    def add_seats(node):
        good_seats.add((node.x, node.y))
        for prev in node.previous:
            add_seats(prev)
    
    for end in end_nodes:
        add_seats(end)

    return len(good_seats)

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
