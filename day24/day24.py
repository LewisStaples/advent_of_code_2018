#!/usr/bin/env python3

# adventOfCode 2018 day 24
# https://adventofcode.com/2018/day/24


def get_input(input_filename):
    the_input = None
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
    print()
    return the_input
    
def solve_problem(input_filename):
    the_input = get_input(input_filename)
    keep_fighting = True
    
    while keep_fighting:
        # Phase 1:  target selection
        # Phase 2:  attacking
        # Dummy stopping condition: combat ends once one army has lost all of its units
        keep_fighting = False

    # Answer: how many units would the winning army have
    return None


solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')


