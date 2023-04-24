#!/usr/bin/env python3

# adventOfCode 2018 day 22
# https://adventofcode.com/2018/day/22


def get_input(input_filename):
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            var_name, var_value = in_string.split(': ')

            if var_name == 'depth':
                depth = int(var_value)
            elif var_name == 'target':
                str_list = var_value.split(',')
                target = tuple([
                    int(ele)
                    for ele in str_list
                ])
    print()
    return depth, target


def get_erosion_level(geologic_index, depth):
    return (geologic_index + depth) % 20183


def get_regional_geologic_indices(depth, target):
    regional_geologic_indices = list()
    MAX_HEIGHT = max(16, target[1])
    MAX_LENGTH = max(16, target[0])
    
    # Top row (height == 0)
    regional_geologic_indices.append(list())
    for length in range(MAX_LENGTH):
        regional_geologic_indices[-1].append(16807 * length)

    # Remaining rows
    for height in range(1, MAX_HEIGHT):
        regional_geologic_indices.append(list())
        regional_geologic_indices[-1].append(48271 * height)
        for length in range(1, MAX_LENGTH):
            regional_geologic_indices[-1].append(
                get_erosion_level(regional_geologic_indices[-1][length - 1], depth)
                * get_erosion_level(regional_geologic_indices[-2][length], depth)
            )
            if (length, height) == target:
                # Set target's geologic index to zero
                regional_geologic_indices[-1][-1] = 0

    return regional_geologic_indices


def display(regional_geologic_indices, target, depth):
    if len(regional_geologic_indices) > 20:
        # Too much data to print on screen !
        return
    for row_num, row in enumerate(regional_geologic_indices):
        for col_num, field in enumerate(row):
            # Print mouth character
            if (col_num, row_num) == (0,0):
                print('M', end = '')
                continue
            # Print target character
            if (col_num, row_num) == target:
                print('T', end = '')
                continue
            
            # Lookup geologic index, calculate erosion level, calculate mod 3 and then match 0,1,2
            match get_erosion_level(regional_geologic_indices[row_num][col_num], depth) % 3:
                # Rocky
                case 0:
                    print('.', end = '')
                # Wet
                case 1:
                    print('=', end = '')
                # Narrow
                case 2:
                    print('|', end = '')
        print()
    print()

def solve_problem(input_filename):
    depth, target = get_input(input_filename)
    regional_geologic_indices = get_regional_geologic_indices(depth, target)
    display(regional_geologic_indices, target, depth)


solve_problem('input_sample0.txt')
