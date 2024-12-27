#!/usr/bin/env python3

# https://adventofcode.com/2024/day/14

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day14.txt')

class Robot():
    def __init__(self, line):
        # One line is like "p=0,4 v=3,-3"
        matches = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
        self.x = int(matches[1])
        self.y = int(matches[2])
        self.dx = int(matches[3])
        self.dy = int(matches[4])

    def move(self, width, height):
        self.x += self.dx
        if self.x < 0:
            self.x = width + self.x
        elif self.x >= width:
            self.x = self.x - width
        
        self.y += self.dy
        if self.y < 0:
            self.y = height + self.y
        elif self.y >= height:
            self.y = self.y - height

def parse_robots(inputfile):
    """Get the list of robots"""
    robots = [Robot(line.strip()) for line in inputfile]
    return robots

def quadrant_scores(robots, width, height):
    # (top-left, top-right, bottom-left, bottom-right)
    mid_x = int(width / 2)
    mid_y = int(height / 2)

    quadrant_1 = 0
    quadrant_2 = 0
    quadrant_3 = 0
    quadrant_4 = 0
    for robot in robots:
        if robot.x < mid_x and robot.y < mid_y:
            quadrant_1 += 1
        elif robot.x > mid_x and robot.y < mid_y:
            quadrant_2 += 1
        elif robot.x < mid_x and robot.y > mid_y:
            quadrant_3 += 1
        elif robot.x > mid_x and robot.y > mid_y:
            quadrant_4 += 1
    return (quadrant_1, quadrant_2, quadrant_3, quadrant_4)

def solve_a(inputfile, width, height, ticks=100):
    """Read the file and return a solution for Part One"""
    robots = parse_robots(inputfile)

    # Simulate robots
    for tick in range(0, ticks):
        for robot in robots:
            robot.move(width, height)

    # Calculate quadrants
    quadrants = quadrant_scores(robots, width, height)
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

def print_robots(robots, width, height):
    for y in range(height):
        for x in range(width):
            is_robot = any(robot.x is x and robot.y is y for robot in robots)
            if is_robot:
                print('X', end='')
            else:
                print('.', end='')
        print()

def is_center_column(robots, width, required=10):
    """See if there are <required> robots in the center column"""
    mid_x = int(width / 2)
    filtered = list(filter(lambda robot: robot.x == mid_x, robots))
    return len(filtered) >= required

def has_center_group(robots, width, height, radius=1):
    """Check if robots fill the full center of the grid"""
    mid_x = int(width / 2)
    mid_y = int(height / 2)
    for x in range(mid_x - radius, mid_x + radius):
        for y in range(mid_y - radius, mid_y + radius):
            if len([True for robot in robots if robot.x == x and robot.y == y]) == 0:
                return False
    return True

def has_quadrant_imbalance(robots, width, height, difference=1):
    # Theory is that the top of the tree will be sparser than the bottom
    quadrants = quadrant_scores(robots, width, height)
    top = quadrants[0] + quadrants[1]
    bottom = quadrants[2] + quadrants[3]

    if top + difference < bottom:
        return True
    else:
        return False

def has_robot(robots, x, y):
    return len([True for robot in robots if robot.x == x and robot.y == y]) > 0

def has_column_anywhere(robots, length=5):
    for robot in robots:
        for y in range(robot.y, robot.y + length):
            if not has_robot(robots, robot.x, y):
                break
            if y + 1 == robot.y + length:
                return True
    return False

def solve_b(inputfile, width, height):
    """Read the file and return a solution for Part Two"""
    robots = parse_robots(inputfile)
    tick = 0
    while True:
        tick += 1
        for robot in robots:
            robot.move(width, height)

        if has_column_anywhere(robots, length=20):
            print_robots(robots, width, height)
            print(f'Tick {tick}')

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile), width=101, height=103)
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile), width=101, height=103)
    print(f'Answer (part B): {answer_b}')
