#!/usr/bin/env python3

# adventOfCode 2018 day 15
# https://adventofcode.com/2018/day/15


TESTING = True



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


def get_adjacent_squares(target_locations, current_state):
    adjacent_squares = set()
    for target_location in target_locations:
        for one_step in [1, -1, -1j,1j]:
            adjacent_squares.add(target_location + one_step)
    return adjacent_squares


# def unit_turn(position, current_state):
def unit_turn(position, target_char, all_units, current_state):
    '''
    This function returns target_position, target_endstate
    '''
    # Final state has been reached if there are no targets left
    if len(all_units[target_char]) == 0:
        return None, None

    adj_open_sq_locations = dict()
    adj_attackable_targets = list()

    # Consider all squares adjacent to a target
    for the_location in get_adjacent_squares(all_units[target_char], current_state):
        if the_location not in current_state:
            continue
        elif current_state[the_location] == '.':
            # It's an adjacent open square, so mark its location
            adj_open_sq_locations[the_location] = None
        elif current_state[the_location][0] == target_char:
            # It's a target that is adjacent to the attacking unit
            adj_attackable_targets.append(the_location)

            

    dummy = 123


    # Identify all targets in range of this unit
    # Identify all open squares in range of a target

    # If any targets are in range, then attack one of them
    # Otherwise take a step towards (one of) the nearest target(s)

    # return target_position, target_endstate
    return None, None


def get_all_units(current_state):
    all_units = {'E': list(), 'G': list(), '.': list()}
    for k,v in current_state.items():
        if type(v) == list:
            all_units[v[0]].append(k)
        elif v == '.':
            all_units[v].append(k)
    return all_units


def do_a_round(current_state):
    next_state = dict()

    next_state['NUM_COLS'] = current_state['NUM_COLS']
    next_state['NUM_ROWS'] = current_state['NUM_ROWS']
    next_state['ROUND_NUMBER'] = current_state['ROUND_NUMBER']
    
    all_units = get_all_units(current_state)

    for row_number in range(current_state['NUM_ROWS']):
        for col_number in range(current_state['NUM_COLS']):
            position = col_number + row_number * 1j
            if position not in current_state:
                continue
            current_value = current_state[position]

            if current_value == '.':
                continue
            else:


                # Identify targets, and their distances
                current_value = current_state[position]
                target_unit = current_value[0]
                target_char = 'G' if target_unit == 'E' else 'E'


                # target_position, target_endstate = unit_turn(position, current_state)
                # There are four possible outcomes:  
                # (1) a target was attacked, 
                # (2) the current unit was moved
                # (3) nothing happened
                # (4) all movement is complete, because there are no targets left
                target_position, target_endstate = unit_turn(position, target_char, all_units, current_state)
                if target_position is None:
                    # This round is incomplete





                    return next_state, False
                next_state[target_position] = target_endstate

                # pass

                # FILL_IN_HERE___PROCESS_THAT_UNIT
    
    # If complete
    # next_state['NUM_COLS'] = current_state['NUM_COLS']
    # next_state['NUM_ROWS'] = current_state['NUM_ROWS']
    next_state['ROUND_NUMBER'] += 1
    # CHANGE THE BELOW False to True, when ready to do so
    return current_state, False


def display(current_state):
    for row_number in range(current_state['NUM_ROWS']):
        for col_number in range(current_state['NUM_COLS']):
            position = col_number + row_number * 1j
            if position not in current_state:
                print('#', end = '')
            else:
                if type(current_state[position]) == list:
                    print(current_state[position][0], end = '')
                else:
                    print(current_state[position], end = '')
        print()
    print()


def get_final_state(current_state):
    keep_going = True
    while keep_going:
        current_state, keep_going = do_a_round(current_state)
        if TESTING and keep_going:
            display(current_state)
    return current_state


def solve_problem(input_filename):
    initial_state = get_initial_state(input_filename)
    final_state = get_final_state(initial_state)


solve_problem('input_sample0.txt')

