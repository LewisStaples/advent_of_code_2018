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
    multiple complex numbers (a + bj), where a is the column number and b is the row number.
    This assumes that the input file will always have a rectangle of characters, and an outer layer (two rows, two columns) of walls.
    '''

    initial_state = {'ROUND_NUMBER':0}

    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for input_row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            if len(in_string) < 15:
                print(in_string)
            for input_col_number, ch in enumerate(in_string):
                if ch == '#':
                    continue
                elif ch == '.':
                    initial_state[(input_col_number - 1) + (input_row_number - 1) * 1j] = '.'
                else:
                    initial_state[(input_col_number - 1) + (input_row_number - 1) * 1j] = [ch, 200]

        
        initial_state['NUM_COLS'] = len(in_string) - 2
        initial_state['NUM_ROWS'] = input_row_number - 1
    print()
    return initial_state

def do_a_round(current_state):
    next_state = dict()
    for row_number in range(current_state['NUM_ROWS']):
        for col_number in range(current_state['NUM_COLS']):
            k = col_number + row_number * 1j
            if k not in current_state:
                continue
            v = current_state[k]
            if k == 'ROUND_NUMBER':
                next_state[k] = current_state[k] + 1
            elif k in ['NUM_COLS', 'NUM_ROWS']:
                next_state[k] = current_state[k]
            elif v == '.':
                continue
            else:
                pass
                # FILL_IN_HERE___PROCESS_THAT_UNIT
        
    # CHANGE THE BELOW False, when ready to do so
    return current_state, False

def get_final_state(current_state):
    keep_going = True
    while keep_going:
        current_state, keep_going = do_a_round(current_state)
    return current_state

def solve_problem(input_filename):
    initial_state = get_initial_state(input_filename)
    final_state = get_final_state(initial_state)

solve_problem('input_sample0.txt')

