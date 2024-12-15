#!/usr/bin/env python3

# https://adventofcode.com/2024/day/11

import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day11.txt')

def parse_stones(inputfile):
    return [int(s) for s in inputfile[0].strip().split()]

cached = {} # (stone, remaining): count
def fancy_blink(stone, remaining):
    global cached

    if remaining == 0:
        return 1
    elif (stone, remaining) in cached:
        return cached[(stone, remaining)]
    else:
        stone_str = str(stone)
        if stone == 0:
            total_stones = fancy_blink(1, remaining-1)
            cached[(stone, remaining)] = total_stones
            return total_stones
        if len(stone_str) % 2 == 0:
            half = int(len(stone_str) / 2)
            first = int(stone_str[0:half])
            second = int(stone_str[half:])

            total_stones = fancy_blink(first, remaining-1) + fancy_blink(second, remaining-1)
            cached[(stone, remaining)] = total_stones
            return total_stones
        else:
            return fancy_blink(stone*2024, remaining-1)
        
def blink(stones):
    length = len(stones)
    index = 0
    while index < length:
        stone = stones[index]
        stone_str = str(stone)
        if stone == 0:
            stones[index] = 1
        elif len(stone_str) % 2 == 0:
            half = int(len(stone_str) / 2)
            first = int(stone_str[0:half])
            second = int(stone_str[half:])
            stones[index] = first
            stones.insert(index+1, second)
            index += 1 # We added an extra stone we want to skip
            length += 1
        else:
            stones[index] = stone * 2024
        index += 1

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    stones = parse_stones(inputfile)
    for count in range(0, 25):
        blink(stones)
    return len(stones)

def solve_b(inputfile, blinks=75):
    """Read the file and return a solution for Part Two"""
    stones = parse_stones(inputfile)
    return functools.reduce(lambda sum, stone: sum + fancy_blink(stone, blinks), stones, 0)

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile).readlines())
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile).readlines())
    print(f'Answer (part B): {answer_b}')
