#!/usr/bin/env python3

# adventOfCode 2018 day 13
# https://adventofcode.com/2018/day/13


import numpy as np


def get_input_line(input_filename):
    tracks = dict()
    carts = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(in_string)
            for col_number, ch in enumerate(in_string):
                if ch in ['v','^']:
                    carts.append([ch,[col_number, row_number]])
                    tracks[(col_number, row_number)]  = ch
                elif ch in ['<','>']:
                    carts.append([ch,[col_number, row_number]])
                    tracks[(col_number, row_number)] = ch
                elif ch == ' ':
                    pass
                else:
                    tracks[(col_number, row_number)] = ch
    print()

    return tracks, [carts]
    
def solve_problem(input_filename):
    tracks, cart_collection_list = get_input_line(input_filename)
    dummy = 123

# solve_problem('input_sample0.txt')

solve_problem('input_sample1.txt')

# solve_problem('input.txt')





