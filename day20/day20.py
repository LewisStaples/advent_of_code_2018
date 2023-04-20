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
    return in_string


def get_vector(ch):
    match ch:
        case 'N': return np.array([0,1])
        case 'E': return np.array([1,0])
        case 'S': return np.array([0,-1])
        case 'W': return np.array([-1,0])
        case _:
            raise ValueError(f'Character {ch} is not a compass direction!')

def get_door(vector):
    if abs(vector[0]) == 1:
        return '|'
    elif abs(vector[1]) == 1:
        return '-'

def add_walls(the_map):

    # Discover the perimeter:
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    for x,y in the_map.keys():
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    # Add outside walls (all one unit outside of the perimeter)
    for x in range(min_x - 1, max_x + 2):
        the_map[(x, min_y - 1)] = '#'
        the_map[(x, max_y + 1)] = '#'
    for y in range(min_y - 1, max_y + 2):
        the_map[(min_x - 1, y)] = '#'
        the_map[(max_x + 1, y)] = '#'

    # Add walls for any spaces that haven't yet been visited
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x,y) not in the_map:
                the_map[(x, y)] = '#'

def get_map(in_string, i_init, curr_locn_in):
    the_map = dict()
    if curr_locn_in is None:
        curr_locn = np.array([0,0])
        the_map[tuple(curr_locn)] = 'X'
    else:
        curr_locn = copy.deepcopy(curr_locn_in)
        
    i = i_init - 1
    while i < len(in_string) - 1:
        i += 1
        if in_string[i] == '(':
            the_map_new, i = get_map(in_string, i + 1, curr_locn)
            the_map |= the_map_new
            continue
        elif in_string[i] == '|':
            curr_locn[0] = curr_locn_in[0]
            curr_locn[1] = curr_locn_in[1]
            continue
        elif in_string[i] in [')','$']:
            break

        try:
            ch_vector = get_vector(in_string[i])
        except IndexError:
            break
        except ValueError:
            # print(f'ValueError occured at character # {i}')
            raise ValueError(f'ValueError occured at character # {i} ... \n\nprior_str: {in_string[:i]}\ntriggering character: {in_string[i]}\npost_str: {in_string[i+1:]}\noriginal_str:{in_string}\n')
        # Add new door to dict the_map
        curr_locn += ch_vector
        the_map[tuple(curr_locn)] = get_door(ch_vector)
        
        # Add new room to dict the_map
        curr_locn += ch_vector
        the_map[tuple(curr_locn)] = '.'

    return the_map, i


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
    add_walls(the_map)
    display(the_map)
    print()

solve_problem('input_sample5.txt')
