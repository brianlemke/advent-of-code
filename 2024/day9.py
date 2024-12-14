#!/usr/bin/env python3

# https://adventofcode.com/2024/day/9

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', default='./inputs/2024_day9.txt')

def unpack_disk_map(map):
    unpacked = [] # File ID or None for each block
    file_id = 0
    is_file = True
    for c in map:
        for i in range(0, int(c)):
            if is_file:
                unpacked.append(int(file_id))
            else:
                unpacked.append(None)
        if is_file:
            file_id += 1
        is_file = not is_file
    return unpacked

def checksum(block_list):
    sum = 0
    for index, id in enumerate(block_list):
        if id is not None:
            sum += id * index
    return sum

def solve_a(inputfile):
    """Read the file and return a solution for Part One"""
    disk_map = [l.strip() for l in inputfile][0]
    block_list = unpack_disk_map(disk_map)

    left = 0
    for right in range(len(block_list) -1, -1, -1):
        if block_list[right] is not None:
            left = block_list.index(None, left)
            if left < right:
                block_list[left] = block_list[right]
                block_list[right] = None

    return checksum(block_list)

def solve_b(inputfile):
    """Read the file and return a solution for Part Two"""
    disk_map = [l.strip() for l in inputfile][0]
    block_list = unpack_disk_map(disk_map)

    def identify_empty_space(needed_size):
        empty_start = block_list.index(None)
        empty_end = 0
        while empty_end - empty_start < needed_size:
            if empty_end == len(block_list):
                return None # Ran out of space to look
            if block_list[empty_end] is not None:
                # This gap is too small, but there might be another one later
                empty_start = empty_end + 1
            empty_end += 1
        return empty_start
    
    cur_file_size = 0
    for right in range(len(block_list) -1, 0, -1):
        if block_list[right] is None:
            cur_file_size = 0
        else:
            cur_file_size += 1
            if block_list[right-1] != block_list[right]:
                # This is the first block in the file, try and find an empty space that can fit it
                empty_start = identify_empty_space(cur_file_size)
                if empty_start is not None and empty_start < right:
                    # Do the copy
                    for i in range(0, cur_file_size):
                        block_list[empty_start + i] = block_list[right + i]
                        block_list[right + i] = None
                cur_file_size = 0
            else:
                # There are more blocks in the file, wait to
                # process it until we get to the start
                pass

    return checksum(block_list)

if __name__ == '__main__':
    args = parser.parse_args()
    answer_a = solve_a(open(args.inputfile))
    print(f'Answer (part A): {answer_a}')
    answer_b = solve_b(open(args.inputfile))
    print(f'Answer (part B): {answer_b}')
