#!/usr/bin/env python3

# https://adventofcode.com/2024/day/15

import argparse
from enum import Enum

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day15.txt')

class Type(Enum):
    Empty = '.'
    Wall = '#'
    Box = 'O'
    Robot = '@'

    BoxLeft = '['
    BoxRight = ']'
    
class Warehouse:
    def __init__(self, grid):
        self.grid = grid

        # Find the grid height and width
        self.height = len(self.grid)
        self.width = len(self.grid[0])

        # Find the initial position of the robot
        for y, row in enumerate(grid):
            for x, t in enumerate(row):
                if t == Type.Robot:
                    self.rx = x
                    self.ry = y
    
    def __str__(self):
        return '\n'.join([''.join([col.value for col in row]) for row in self.grid])
    
    def move_func(self, x, y, gen_next_coord):
        nx, ny = gen_next_coord(x, y)
        if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
            return False # out of bounds
        elif self.grid[ny][nx] == Type.Empty:
            self.grid[ny][nx] = self.grid[y][x]
            self.grid[y][x] = Type.Empty
            return True
        elif self.grid[ny][nx] == Type.Box:
            if self.move_func(nx, ny, gen_next_coord):
                self.grid[ny][nx] = self.grid[y][x]
                self.grid[y][x] = Type.Empty
                return True
            else:
                return False
        else:
            return False # Probably a wall
    
    def move_left(self):
        if self.move_func(self.rx, self.ry, lambda x, y: (x-1,y)):
            self.rx -= 1

    def move_up(self):
        if self.move_func(self.rx, self.ry, lambda x, y: (x,y-1)):
            self.ry -= 1

    def move_right(self):
        if self.move_func(self.rx, self.ry, lambda x, y: (x+1,y)):
            self.rx += 1

    def move_down(self):
        if self.move_func(self.rx, self.ry, lambda x, y: (x,y+1)):
            self.ry += 1

class Direction(Enum):
    Left = '<'
    Up = '^'
    Right = '>'
    Down = 'v'

class DoubleWarehouse:
    def __init__(self, grid):
        self.grid = grid

        # Double the grid
        for row in self.grid:
            for x in range(0, len(row)):
                match row[x*2]:
                    case Type.Wall:
                        row.insert(x*2 + 1, Type.Wall)
                    case Type.Empty:
                        row.insert(x*2 + 1, Type.Empty)
                    case Type.Robot:
                        row.insert(x*2 + 1, Type.Empty)
                    case Type.Box:
                        row[x*2] = Type.BoxLeft
                        row.insert(x*2 + 1, Type.BoxRight)

        # Find the grid height and width
        self.height = len(self.grid)
        self.width = len(self.grid[0])

        # Find the initial position of the robot
        for y, row in enumerate(self.grid):
            for x, t in enumerate(row):
                if t == Type.Robot:
                    self.rx = x
                    self.ry = y

    def __str__(self):
        return '\n'.join([''.join([col.value for col in row]) for row in self.grid])
    
    def move_func(self, x, y, direction, dry_run=False):
        def gen_next_coord(x, y):
            match direction:
                case Direction.Left:
                    return (x-1, y)
                case Direction.Up:
                    return (x, y-1)
                case Direction.Right:
                    return (x+1, y)
                case Direction.Down:
                    return (x, y+1)
        
        nx, ny = gen_next_coord(x, y)
        if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
            return False # out of bounds
        elif self.grid[ny][nx] == Type.Empty:
            if not dry_run:
                self.grid[ny][nx] = self.grid[y][x]
                self.grid[y][x] = Type.Empty
            return True
        elif self.grid[ny][nx] == Type.Wall:
            return False
        elif direction == Direction.Left or direction == Direction.Right:
            # This is the simple case of moving boxes
            if self.move_func(nx, ny, direction, dry_run):
                if not dry_run:
                    self.grid[ny][nx] = self.grid[y][x]
                    self.grid[y][x] = Type.Empty
                return True
            else:
                return False
        else:
            # This is the complicated case of moving boxes, need
            # to check both sides
            bny = ny
            bnx = nx + 1 if self.grid[ny][nx] == Type.BoxLeft else nx - 1

            if self.move_func(nx, ny, direction, dry_run) and self.move_func(bnx, bny, direction, dry_run):
                if not dry_run:
                    self.grid[ny][nx] = self.grid[y][x]
                    self.grid[y][x] = Type.Empty
                return True
            else:
                return False

    def move_left(self):
        if self.move_func(self.rx, self.ry, Direction.Left, dry_run=True):
            self.move_func(self.rx, self.ry, Direction.Left)
            self.rx -= 1

    def move_up(self):
        if self.move_func(self.rx, self.ry, Direction.Up, dry_run=True):
            self.move_func(self.rx, self.ry, Direction.Up)
            self.ry -= 1

    def move_right(self):
        if self.move_func(self.rx, self.ry, Direction.Right, dry_run=True):
            self.move_func(self.rx, self.ry, Direction.Right)
            self.rx += 1

    def move_down(self):
        if self.move_func(self.rx, self.ry, Direction.Down, dry_run=True):
            self.move_func(self.rx, self.ry, Direction.Down)
            self.ry += 1

def parse_input(inputfile):
    """Return (grid, instructions) where instructions is a string"""

    grid = [] # Array of rows, which has an array of columns, which are a Type
    instructions = ""
    is_instructions = False # Switch modes at the empty line
    for line in inputfile:
        l = line.strip()
        if len(l) == 0:
            is_instructions = True
        elif is_instructions:
            instructions += l
        else:
            grid.append([Type(ch) for ch in l])
    return (grid, instructions)

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    grid, instructions = parse_input(inputfile)
    warehouse = Warehouse(grid)

    for i in instructions:
        # print(str(warehouse))
        # print(f"Next instruction: {i}")
        match i:
            case '<':
                warehouse.move_left()
            case '^':
                warehouse.move_up()
            case '>':
                warehouse.move_right()
            case 'v':
                warehouse.move_down()
            case _:
                raise Exception("Unknown instruction")
    
    # Calculate the score
    score = 0
    for y, row in enumerate(warehouse.grid):
        for x, val in enumerate(row):
            if val == Type.Box:
                score += 100*y + x
    return score

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    grid, instructions = parse_input(inputfile)
    warehouse = DoubleWarehouse(grid)

    for i in instructions:
        # print(str(warehouse))
        # print(f"Next instruction: {i}")
        match i:
            case '<':
                warehouse.move_left()
            case '^':
                warehouse.move_up()
            case '>':
                warehouse.move_right()
            case 'v':
                warehouse.move_down()
            case _:
                raise Exception("Unknown instruction")
    
    # Calculate the score
    score = 0
    for y, row in enumerate(warehouse.grid):
        for x, val in enumerate(row):
            if val == Type.BoxLeft:
                score += 100*y + x
    return score

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
