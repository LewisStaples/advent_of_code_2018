#!/usr/bin/env python3

# adventOfCode 2018 day 17
# https://adventofcode.com/2018/day/17


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_clay_coords(input_filename):
    clay_coords = set()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            singleton_str, range_str = in_string.rstrip().split(', ')

            const_var_str = singleton_str[0]
            const_var = int(singleton_str[2:])
            globals()[const_var_str] = const_var
            
            loop_var_str = range_str[0]
            loop_lower, loop_upper = range_str.split('=')[1].split('..')
            for loop_var in range(int(loop_lower), int(loop_upper) + 1):
                globals()[loop_var_str] = loop_var
                clay_coords.add((x,y))

            # print(in_string)
    # print()
    return clay_coords
    
def solve_problem(input_filename):
    clay_coords = get_clay_coords(input_filename)



solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')





