#!/usr/bin/env python3

# https://adventofcode.com/2024/day/10

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2025_day10.txt')

class MachineDefinition:
    def __init__(self, line):
        parts = line.split()
        self.lights = tuple([x == '#' for x in parts[0][1:-1]])
        self.joltages = tuple([int(x) for x in ''.join(parts[-1][1:-1]).split(',')])
        self.buttons = [tuple([int(x) for x in p[1:-1].split(',')]) for p in parts[1:-1]]

def solve_indicator_lights(machine):
    # BFS

    # Track every state we've reached before. If a button press results in
    # one of these states, we know it is less optimal than a previous sequence
    attained_states: set[tuple] = set()

    # Initialize to all off
    attained_states.add(tuple([False for _ in machine.lights]))
    presses = 0
    current_states: set[tuple] = attained_states.copy()

    while True: # We have to eventually solve the machine and return
        new_states: set[tuple] = set()
        for state in current_states:
            if state == machine.lights:
                return presses
            
            for button in machine.buttons:
                new_state = tuple([not l if i in button else l for i, l in enumerate(state)])
                if new_state not in attained_states:
                    attained_states.add(new_state)
                    new_states.add(new_state)

        current_states = new_states.copy()
        presses += 1
    
def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    machines = [MachineDefinition(line.strip()) for line in inputfile]
    total = 0
    for m in machines:
        solution = solve_indicator_lights(m)
        total += solution
    return total


def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    return None

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
