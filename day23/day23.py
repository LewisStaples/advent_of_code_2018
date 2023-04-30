#!/usr/bin/env python3

# adventOfCode 2018 day 23
# https://adventofcode.com/2018/day/23


def get_input_line(input_filename):
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()

            # Input line into data structures
            print(in_string)
    print()
    
    # ADD ... return data structures with lines of input
    
def solve_problem(input_filename):
    in_string = get_input_line(input_filename)
    # Determine the largest value of r, and the associated pos value
    
    # Calculate Manhattan distances for each pos from the largest r's pos
    # If Manhattan distance is <= largest r, then this nanobot is in range.
    # Otherwise, it is not.
    


solve_problem('input.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')
