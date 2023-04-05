#!/usr/bin/env python3

# adventOfCode 2018 day 18
# https://adventofcode.com/2018/day/18


def get_input(input_filename):
    lumber_collection_area = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            lumber_collection_area.append(list(in_string))
    print()
    return lumber_collection_area
    
def solve_problem(input_filename):
    lca_pair = [None, None]
    lca_pair[0] = get_input(input_filename)

    for minutes_passed in range(1, 11):
        # Demonstration only ... actual logic is more complicated
        lca_pair[minutes_passed % 2] = lca_pair[(minutes_passed - 1) % 2]

solve_problem('input_sample0.txt')
