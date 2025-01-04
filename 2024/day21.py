#!/usr/bin/env python3

# https://adventofcode.com/2024/day/21

import argparse
import re
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day21.txt')

class Keypad:
    def __init__(self, grid, name, controller):
        self.grid = grid
        self.name = name
        self.controller = controller
        self.presses = ''
        self.stored_pos = []

        self.lookup = dict()
        for row, r in enumerate(self.grid):
            for col, v in enumerate(r):
                self.lookup[v] = (row, col)

        self.pos = self.coords('A')

    def coords(self, value):
        return self.lookup[value]
    
    def current(self):
        return self.grid[self.pos[0]][self.pos[1]]
    
    def store_state(self):
        self.stored_pos.append(self.pos)
        if self.controller != None:
            self.controller.store_state()
    
    def restore_state(self):
        self.pos = self.stored_pos.pop()
        if self.controller != None:
            self.controller.restore_state()
    
    def press(self):
        # print(f'{self.name}:\t{self.current()}')
        self.presses += self.current()
    
    def make_move(self, move):
        self.pos = self.try_move(self.pos, move)
    
    def try_move(self, start, move):
        (row, col) = start
        match move:
            case '<':
                return (row,col-1)
            case '^':
                return (row-1,col)
            case '>':
                return (row,col+1)
            case 'v':
                return (row+1,col)
    
    def find_navigation_sequences(self, target_val):
        """Find the shortest sequences from pos to target, avoiding None, and grouping the same direction together"""
        target_coords = self.coords(target_val)
        dy = target_coords[0] - self.pos[0] # Positive means go down, negative means go up
        dx = target_coords[1] - self.pos[1] # Positive means go right, negative means go left
        row_moves = ('<' if dx < 0 else '>') * abs(dx)
        col_moves = ('^' if dy < 0 else 'v') * abs(dy)

        candidates = [row_moves + col_moves, col_moves + row_moves]
        sequences = [c for c in candidates if self.is_valid_sequence(c)]
        return sequences
    
    def is_valid_sequence(self, sequence):
        """Make sure the sequence doesn't go through None"""
        cur = self.pos
        for move in sequence:
            cur = self.try_move(cur, move)
            if self.grid[cur[0]][cur[1]] is None:
                return False
        return True

class NumericKeypad(Keypad):
    def __init__(self, name, controller=None):
        grid = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            [None, '0', 'A'],
        ]
        Keypad.__init__(self, grid, name, controller)
    
class DirectionalKeypad(Keypad):
    def __init__(self, name, controller=None):
        grid = [
            [None, '^', 'A'],
            ['<', 'v', '>'],
        ]
        Keypad.__init__(self, grid, name, controller)

@functools.cache
def solve_move(move, start, robot_keypads):
    if robot_keypads == 0:
        return 1
    
    keypad = DirectionalKeypad("current")
    keypad.pos = keypad.coords(start)
    sequences = keypad.find_navigation_sequences(move)
    best_moves = None
    for sequence in sequences:
        num_moves = 0
        next_keypad = DirectionalKeypad("next")
        for m in sequence:
            num_moves += solve_move(m, next_keypad.current(), robot_keypads-1)
            next_keypad.pos = next_keypad.coords(m)
        num_moves += solve_move('A', next_keypad.current(), robot_keypads-1)
        if best_moves is None or num_moves < best_moves:
            best_moves = num_moves

    return best_moves

def solve_code_2(code, robot_keypads=2):
    """Return the sequence of button presses to solve the code"""
    # Only the first directional keypad matters because it is the
    # only one that won't end on 'A' after each move
    numeric = NumericKeypad("numeric")

    num_presses = 0
    for val in code:
        sequences = numeric.find_navigation_sequences(val)
        best_presses = None
        for sequence in sequences:
            numeric.store_state()
            presses = 0
            next_keypad = DirectionalKeypad("next")
            for m in sequence:
                presses += solve_move(m, next_keypad.current(), robot_keypads)
                next_keypad.pos = next_keypad.coords(m)
            presses += solve_move('A', next_keypad.current(), robot_keypads)
            numeric.restore_state()

            if best_presses is None or presses < best_presses:
                best_presses = presses
        numeric.pos = numeric.coords(val)
        num_presses += best_presses

    return num_presses

def solve_code(code):
    """Return the sequence of button presses to solve the code"""
    third = DirectionalKeypad("third")
    second = DirectionalKeypad("second", controller=third)
    first = NumericKeypad("first", controller=second)

    def press_button(keypad, value):
        if keypad is None:
            # print(f'human:\t{value}')
            return value
        
        # Identify the best sequence first
        best_presses = None
        best_sequence = None
        sequences = keypad.find_navigation_sequences(value)
        for sequence in sequences:
            keypad.store_state()
            presses = ''
            for move in sequence:
                presses += press_button(keypad.controller, move)
                keypad.make_move(move)
            presses += press_button(keypad.controller, 'A')
            keypad.restore_state()

            if best_presses is None or len(presses) < len(best_presses):
                best_presses = presses
                best_sequence = sequence

        # Now apply the best sequence for real
        for move in sequence:
            press_button(keypad.controller, move)
            keypad.make_move(move)
        press_button(keypad.controller, 'A')

        return best_presses

    final_sequence = ''
    for val in code:
        final_sequence += press_button(first, val)

    return final_sequence

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    codes = [line.strip() for line in inputfile]

    sum = 0
    for code in codes:
        sequence = solve_code(code)
        presses = len(sequence)
        numeric_part = int(re.search(r'\d+', code).group())
        complexity = numeric_part * presses
        sum += complexity
    return sum

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    codes = [line.strip() for line in inputfile]

    sum = 0
    for code in codes:
        presses = solve_code_2(code, 25)
        numeric_part = int(re.search(r'\d+', code).group())
        complexity = numeric_part * presses
        sum += complexity
    return sum

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
