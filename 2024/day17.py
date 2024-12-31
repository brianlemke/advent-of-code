#!/usr/bin/env python3

# https://adventofcode.com/2024/day/17

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day17.txt')

class DebuggerOutput:
    def __init__(self, inputfile=None):
        if inputfile is not None:
            self.parse_input(inputfile)
        else:
            self.a = 0
            self.b = 0
            self.c = 0
            self.instructions = []
    
    def parse_input(self, inputfile):
        lines = [line.strip() for line in inputfile]
        re_register = r'Register .: (\d+)'
        self.a = int(re.match(re_register, lines[0])[1])
        self.b = int(re.match(re_register, lines[1])[1])
        self.c = int(re.match(re_register, lines[2])[1])

        program = lines[4].split(' ')[1]
        self.instructions = [int(ch) for ch in program.split(',')]


class Computer:
    def __init__(self, debugger):
        self.a = debugger.a
        self.b = debugger.b
        self.c = debugger.c
        self.ip = 0
        self.output = []
    
    def pretty_output(self):
        return ','.join(self.output)
    
    def get_combo_op(self, operand):
        if operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        else:
            return operand

    def process(self, instructions, required_output=None):
        # Process the instructions
        while self.ip < len(instructions) - 1:
            opcode = instructions[self.ip]
            operand = instructions[self.ip+1]
            match opcode:
                case 0: # adv - division
                    self.a = int(self.a / pow(2, self.get_combo_op(operand)))
                case 1: # bxl - bitwise xor
                    self.b = self.b ^ operand
                case 2: # bst - modulo
                    self.b = self.get_combo_op(operand) % 8
                case 3: # jnz - jump
                    if self.a != 0:
                        self.ip = operand
                        continue
                case 4: # bxc - bitwise xor
                    self.b = self.b ^ self.c
                case 5: # out - output
                    val = self.get_combo_op(operand) % 8
                    # abort if we're about to output something wrong
                    if required_output != None:
                        if len(required_output) > 0:
                            required = required_output.pop(0)
                            if required != val:
                                return False
                        else:
                            return False
                    self.output.append(str(val))
                case 6: # bdv - division
                    self.b = int(self.a / pow(2, self.get_combo_op(operand)))
                case 7: # cdv - division
                    self.c = int(self.a / pow(2, self.get_combo_op(operand)))
            self.ip += 2
        return True

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    debugger = DebuggerOutput(inputfile)
    pc = Computer(debugger)
    pc.process(debugger.instructions)
    return pc.pretty_output()

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    debugger = DebuggerOutput(inputfile)
    instructions = ','.join([str(ch) for ch in debugger.instructions])
    replacement_a = 0
    while True:
        pc = Computer(debugger)
        pc.a = replacement_a
        success = pc.process(debugger.instructions, required_output=debugger.instructions.copy())
        if success and pc.pretty_output() == instructions:
            return replacement_a
        replacement_a += 1

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
