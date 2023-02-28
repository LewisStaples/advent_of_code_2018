#!/usr/bin/env python3

# adventOfCode 2018 day 15
# https://adventofcode.com/2018/day/15


def get_initial_state(input_filename):
    '''
    This reads the input file and returns a dict that describes the initial state
    The keys in this dict will be:
    ROUND_NUMBER, which is the current round number (initiallly zero)
    NUM_ROWS, which is the number of rows within the rectangle where action can happen
    NUM_COLS, which is the number of columns within the rectangle where action can happen
    a complex number (a + bj), where a is the column number and b is the row number.
    This assumes that the input file will always have a rectangle of characters, and an outer layer (two rows, two columns) of walls.
    '''

    initial_state = {'ROUND_NUMBER':0}

    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for input_row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(in_string)
            for input_col_number, ch in enumerate(in_string):
                if ch == '#':
                    continue
                initial_state[(input_col_number - 1) + (input_row_number - 1) * 1j] = ch

        
        initial_state['NUM_COLS'] = len(in_string) - 2
        initial_state['NUM_ROWS'] = input_row_number - 1
    print()
    return initial_state
    
def solve_problem(input_filename):
    current_state = get_initial_state(input_filename)

solve_problem('input_sample0.txt')

