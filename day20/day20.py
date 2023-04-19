#!/usr/bin/env python3

# adventOfCode 2018 day 20
# https://adventofcode.com/2018/day/20


import numpy as np
import copy

def get_input_line(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f'The original input is: {in_string}')
    # return in_string[1:-1]
    return in_string


def get_vector(ch):
    match ch:
        case 'N': return np.array([0,1])
        case 'E': return np.array([1,0])
        case 'S': return np.array([0,-1])
        case 'W': return np.array([-1,0])
        case '$': return np.array([0,0])
        case ')': return np.array([0,0])
        case _:
            # return np.array([0,0])
            raise ValueError(f'Character {ch} is not a compass direction!')

def get_door(vector):
    if abs(vector[0]) == 1:
        return '|'
    elif abs(vector[1]) == 1:
        return '-'

def get_map(in_string, i_init, curr_locn_in):
    ret_val = dict()
    if curr_locn_in is None:
        curr_locn = np.array([0,0])
        ret_val[tuple(curr_locn)] = 'X'
    else:
        curr_locn = copy.deepcopy(curr_locn_in)
        
        dummy = 123

    # for i in range(i_init,len(in_string) + 1):
    i = i_init - 1
    while i < len(in_string) - 1:
        i += 1
        if in_string[i] == '(': # in ['(','|']:
            ret_val_new, i = get_map(in_string, i + 1, curr_locn)
            ret_val |= ret_val_new
        elif in_string[i] == '|':
            curr_locn[0] = curr_locn_in[0]
            curr_locn[1] = curr_locn_in[1]
            continue
            # try:
            #     if in_string[i] == '|':
            #         i -= 1
            #     break
            # except IndexError:
            #     break
        elif in_string[i] in [')','$']:
            break

        try:
            ch_vector = get_vector(in_string[i])
        except IndexError:
            break
        # Add new door to dict ret_val
        curr_locn += ch_vector
        ret_val[tuple(curr_locn)] = get_door(ch_vector)
        
        # Add new room to dict ret_val
        curr_locn += ch_vector
        ret_val[tuple(curr_locn)] = '.'

        # Test both above to see if they're already there, and then test for any contradiction

    return ret_val, i + 1


def display(the_map):
    print('-------------------')
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    for x,y in the_map.keys():
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)


    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x,y) in the_map:
                print(the_map[(x,y)][0], end = '')
            else:
                print(' ', end = '')
        print()
    print('-------------------')

def solve_problem(input_filename):
    in_string = get_input_line(input_filename)
    the_map, _ = get_map(in_string, 1, None)
    display(the_map)
    print(f'Without start and end characters: {in_string}')
    print()

solve_problem('input_sample2.txt')
