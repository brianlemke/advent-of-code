#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--day', required=True)
parser.add_argument('-y', '--year', default='2025')

DAY_MARKER = 'REPLACEME'

def copy_and_replace(src, dest, day):
    """Copy a template file and replace placeholders with the day"""
    with open(src, 'r') as infile:
        file = infile.read()
    file = file.replace(DAY_MARKER, day)
    with open(dest, 'w') as outfile:
        outfile.write(file)

def create_day(day, year):
    script_dir = os.path.dirname(os.path.realpath(__file__))

    template_main = os.path.join(script_dir, 'dayx.py')
    template_test = os.path.join(script_dir, 'dayx_test.py')

    main_file = os.path.join(script_dir, year, f'day{day}.py')
    test_file = os.path.join(script_dir, year, f'day{day}_test.py')
    input_file = os.path.join(script_dir, 'inputs', f'{year}_day{day}.txt')

    print(f'Creating new day\nScript\t: {main_file}\nTest\t: {test_file}\nInput\t: {input_file}')
    copy_and_replace(template_main, main_file, day)
    copy_and_replace(template_test, test_file, day)

    # Touch the input file
    open(input_file, 'w')

if __name__ == '__main__':
    args = parser.parse_args()
    create_day(args.day, args.year)
