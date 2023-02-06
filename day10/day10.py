#!/usr/bin/env python3

# adventOfCode 2018 day 10
# https://adventofcode.com/2018/day/10

import numpy as np
from collections import deque 



def str_to_list(in_string):
    the_list = list(in_string.split(', '))
    return [int(x) for x in the_list]


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

            positions.append(str_to_list(l_string))
            velocities.append(str_to_list(r_string))

            # print(l_string)
            # print(r_string)
    # print()
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

def display(positions, title):
    bounding_box = get_bounding_box(positions)
    # print(f'Bounding box: {bounding_box}\n')
    print(title)
    for y in range(bounding_box['smallest_y'], bounding_box['largest_y'] + 1):
        for x in range(bounding_box['smallest_x'], bounding_box['largest_x'] + 1):
            if [x,y] in positions:
                print('#', end= '')
            else:
                print('.', end= '')
        print()
    print()

def count_positions_on_bounding_box(positions, bounding_box):
    '''
    Note that any positions in a corner will get counted twice.
    (That is immaterial, since what matters is to detect the 
    spike in this value when the problem is solved)
    '''
    ret_val = 0
    for position in positions:
        for the_label, rhs_value in bounding_box.items():
            if position[ord(the_label[-1]) - ord('x')] == rhs_value:
                ret_val += 1
    return ret_val

def bounding_box_length(bounding_box):
    return 2 * (bounding_box['largest_x'] - bounding_box['smallest_x'] + bounding_box['largest_y'] - bounding_box['smallest_y'])

def bounding_box_area(bounding_box):
    return (bounding_box['largest_x'] - bounding_box['smallest_x']) + (bounding_box['largest_y'] - bounding_box['smallest_y'])


def completed(positions, time_elapsed, last_three_bba):
    # print(f'Time elapsed: {time_elapsed}      ', end = '')
    bounding_box = get_bounding_box(positions)

    count_of_POBB = count_positions_on_bounding_box(positions, bounding_box)
    # print(f'count of POBB = {count_of_POBB}')

    bbl = bounding_box_length(bounding_box)
    # print(f'bbl = {bbl}')

    bba = bounding_box_area(bounding_box)
    # print(f'bba = {bba}')

    last_three_bba.append(bba)
    last_three_bba.popleft()

    if last_three_bba[1] < min(last_three_bba[0], last_three_bba[2]):
        print(f'Display using time:  {time_elapsed}')
        return True
    dummy = 123


    # print('calling completed function ....')

    # print()



def next_step(positions, velocities, step = 1):
    ret_val = list()
    for the_index in range(len(positions)):
        ret_val.append(
            [
                positions[the_index][0] + step * velocities[the_index][0] ,
                positions[the_index][1] + step * velocities[the_index][1]
            ]
        )
    return ret_val

def solve_problem(input_filename):
    positions, velocities = get_input(input_filename)
    # display(positions, 'Initial Positions')
    time_elapsed = 0
    last_three_bba = deque([float('inf'), float('inf'), float('inf')])
    while True:
        time_elapsed += 1
        positions = next_step(positions, velocities)
        # display(positions, f'Positions after time {time_elapsed} has elapsed')
        # if time_elapsed > 25:
            # break
        if completed(positions, time_elapsed, last_three_bba):
            break
    
    positions = next_step(positions, velocities, -1)
    display(positions, 'Final Positions')
    print()
solve_problem('input.txt')
