#!/usr/bin/env python3

# https://adventofcode.com/2024/day/6

import argparse
from enum import Enum
from copy import deepcopy
from utilities import print_progress_bar

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day6.txt')

class Point:
    def __init__(self, is_obstacle):
        self.is_obstacle = is_obstacle
        self.visited = False
        self.visited_orientations = []

class Orientation(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Guard:
    def __init__(self, x, y, orientation=Orientation.UP):
        self.x = x
        self.y = y
        self.orientation = orientation
    
    def tuple(self):
        """Get the guard's status as a tuple for hashing"""
        return (self.x, self.y, self.orientation)

    def get_next_move(self):
        """Determine the guard's next move if nothing is in the way"""
        match self.orientation:
            case Orientation.UP:
                return (self.x, self.y-1)
            case Orientation.RIGHT:
                return (self.x+1, self.y)
            case Orientation.DOWN:
                return (self.x, self.y+1)
            case Orientation.LEFT:
                return (self.x-1, self.y)
    
    def move(self):
        x,y = self.get_next_move()
        self.x = x
        self.y = y
            
    def rotate(self):
        match self.orientation:
            case Orientation.UP:
                self.orientation = Orientation.RIGHT
            case Orientation.RIGHT:
                self.orientation = Orientation.DOWN
            case Orientation.DOWN:
                self.orientation = Orientation.LEFT
            case Orientation.LEFT:
                self.orientation = Orientation.UP

class Map:
    def __init__(self, input):
        self.points = {} # (x,y) => Point
        self.guard = None

        # Parse input into rows
        rows = [r.strip() for r in input]

        # Create points and identify the guard
        for y, row in enumerate(rows):
            for x, col in enumerate(row):
                point = Point(is_obstacle = (col == '#'))
                if col == '^':
                    point.visited = True
                    point.visited_orientations.append(Orientation.UP)
                    self.guard = Guard(x, y)
                self.points[(x,y)] = point
    
    def get_point(self, coords):
        return self.points.get(coords, None)

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    map = Map(inputfile)
    while map.guard:
        next_coords = map.guard.get_next_move()
        next_point = map.get_point(next_coords)
        if next_point:
            if next_point.is_obstacle:
                map.guard.rotate()
            else:
                map.guard.move()
                next_point.visited = True
        else:
            map.guard = None # We're done, guard is off the map
    
    # Count how many points have been visited
    count = 0
    for _, point in map.points.items():
        if point.visited:
            count += 1
    return count

def is_cycle(map):
    """Determine whether the guard gets stuck in a cycle on the provided map"""
    while map.guard:
        next_coords = map.guard.get_next_move()
        next_point = map.get_point(next_coords)
        cur_point = map.get_point((map.guard.x, map.guard.y))
        if next_point:
            if next_point.is_obstacle:
                map.guard.rotate()
                if map.guard.orientation in cur_point.visited_orientations:
                    break
                else:
                    cur_point.visited_orientations.append(map.guard.orientation)
            else:
                map.guard.move()
                next_point.visited = True
                if map.guard.orientation in next_point.visited_orientations:
                    break
                else:
                    next_point.visited_orientations.append(map.guard.orientation)
        else:
            map.guard = None # We're done, guard is off the map
    return map.guard != None

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    map = Map(inputfile)

    # Progress tracker
    total = len(map.points)
    current = 0

    # Attempt to add an obstacle to each location and check if the map is a cycle
    sum = 0
    for coord, point in map.points.items():
        current += 1
        print_progress_bar(current, total)
        if point.is_obstacle or point.visited:
            # Short-circuit, can't add an obstacle here
            continue
        copy = deepcopy(map)
        copy.points[coord].is_obstacle = True
        if is_cycle(copy):
            sum += 1
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
