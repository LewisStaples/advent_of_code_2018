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

            print(l_string)
            print(r_string)
    print()
    return positions, velocities

def get_bounding_box(positions):
    return_value = {
        'smallest_x': float('inf'),
        'largest_x': float('-inf'),
        'smallest_y': float('inf'),
        'largest_y': float('-inf'),
        }
    for x,y in positions:
        return_value['smallest_x'] = min(return_value['smallest_x'], x)
        return_value['largest_x'] = max(return_value['largest_x'], x)
        return_value['smallest_y'] = min(return_value['smallest_y'], y)
        return_value['largest_y'] = max(return_value['largest_y'], y)
    return return_value

def display(positions):
    bounding_box = get_bounding_box(positions)
    print(f'Bounding box: {bounding_box}\n')
    
    for y in range(bounding_box['smallest_y'], bounding_box['largest_y'] + 1):
        for x in range(bounding_box['smallest_x'], bounding_box['largest_x'] + 1):
            print('.', end = '')
        print()
    print()


            # BELOW CODE TRIGGERING AN ERROR .... DETERMINE ALTERNATIVE ....
            # if np.array([x,y]) in positions:
            #     print('#')
            # else:
            #     print('.')

def solve_problem(input_filename):
    positions, velocities = get_input(input_filename)
    display(positions)


solve_problem('input_sample0.txt')


    

