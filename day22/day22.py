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

def solve_problem(input_filename):
    depth, target = get_input(input_filename)
    print(f'{depth = }')
    print(f'{target = }')
    print()

solve_problem('input_sample0.txt')
