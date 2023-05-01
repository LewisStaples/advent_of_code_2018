#!/usr/bin/env python3

# adventOfCode 2018 day 23
# https://adventofcode.com/2018/day/23


def get_input_DSs(input_filename):
    pos_list = list()
    r_list = list()

    # Reading input
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()

            # Input line into data structures
            left_str, r_str = in_string.split(', r=')
            pos_str = left_str[5:-1].split(',')
            print(f'{in_string}   pos: {pos_str}   r: {r_str}')
            r_list.append(int(r_str))

            pos = tuple([
                int(x)
                for x in pos_str
            ])
            pos_list.append(pos)

    r_max = max(r_list)
    index__r_max = r_list.index(r_max)
    print(f'Maximum r: {r_max}, Associated POS: {pos_list[index__r_max]}')
    print()
    
    # ADD ... return data structures with lines of input
    return r_list, pos_list
    
def solve_problem(input_filename):
    r_list, pos_list = get_input_DSs(input_filename)

    # Determine the largest value of r, and the associated pos value
    
    # Calculate Manhattan distances for each pos from the largest r's pos
    # If Manhattan distance is <= largest r, then this nanobot is in range.
    # Otherwise, it is not.
    


solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')
