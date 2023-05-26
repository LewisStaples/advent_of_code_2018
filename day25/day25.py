#!/usr/bin/env python3

# adventOfCode 2018 day 25
# https://adventofcode.com/2018/day/25


def get_constellation_count(input_filename):
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            this_point = [int(x) for x in in_string.rstrip().split(',')]
            print(this_point)
    print()

    return 42
    
constellation_count = get_constellation_count('input_sample0.txt')
print(f'The number of constellations is: {constellation_count}')

