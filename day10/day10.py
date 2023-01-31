#!/usr/bin/env python3

# adventOfCode 2018 day 10
# https://adventofcode.com/2018/day/10

import numpy as np

# POTENTIAL ALTERNATIVE FOR MU
# TLIPLE LINE INPUT FILES ....

def str_to_np_array(in_string):
    the_list = list(in_string.split(', '))
    the_list = [int(x) for x in the_list]
    return np.array(the_list)

def get_input(input_filename):
    positions = list()
    velocities = list()

    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            l_string, r_string = in_string.rstrip().split('> velocity=<')
            l_string = l_string[10:]
            r_string = r_string[:-1]

            positions.append(str_to_np_array(l_string))
            velocities.append(str_to_np_array(r_string))

    return positions, velocities

    
def solve_problem(input_filename):
    positions, velocities = get_input(input_filename)


solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')
    

