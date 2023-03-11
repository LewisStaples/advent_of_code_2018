#!/usr/bin/env python3

# adventOfCode 2018 day 15
# https://adventofcode.com/2018/day/15


# There are five possible outcomes when a particular unit takes its turn:  
# (1) a target was attacked but not killed, 
# (2) a target was attacked and killed off, 
# (3) the current unit was moved
# (4) nothing happened
# (5) there are no targets left

# import numpy as np

import enum
class UnitTurnOutcome(enum.Enum):
    TARGET_ATTACKED_ALIVE = 1
    TARGET_KILLED = 2
    CURRENT_UNIT_MOVED = 3
    NOTHING_HAPPENED = 4
    NO_TARGETS_LEFT = 5

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
                # if ch == '#':
                #     continue
                # elif ch == '.':
                #     initial_state[(input_col_number - 1) + (input_row_number - 1) * 1j] = '.'
                if ch == '.':
                    continue
                elif ch == '#':
                    initial_state[(input_col_number - 1) + (input_row_number - 1) * 1j] = '#'
                else:
                    # initial_state[(input_col_number - 1) + (input_row_number - 1) * 1j] = [ch, 200]
                    initial_state[(input_col_number - 1) + (input_row_number - 1) * 1j] = {'char': ch, 'hit_points': 200, 'attack_power': 3}

        
        initial_state['NUM_COLS'] = len(in_string) - 2
        initial_state['NUM_ROWS'] = input_row_number - 1
    print()
    return initial_state


def get_adjacent_squares(target_locations):
    adjacent_squares = set()
    for target_location in target_locations:
        for one_step in [1, -1, -1j,1j]:
            adjacent_squares.add(target_location + one_step)
    return adjacent_squares


def first__reading_order(position_iterable):
    # Initially consider the 0-th element to be the first in "reading order"
    ret_val = position_iterable[0]
    # Then compare the value of each remaining element to ret_val.
    # Reassign ret_val to the newly checked element if its reading order comes ahead of it
    for i in range(1, len(position_iterable)):
        if position_iterable[i].imag < ret_val.imag:
            ret_val = position_iterable[i]
        if position_iterable[i].imag == ret_val.imag and position_iterable[i].real < ret_val.real:
            ret_val = position_iterable[i]
    return ret_val



def unit_turn(position_player, target_char, all_units, current_state):
    '''
    This function returns target_position, target_endstate
    '''
    # Final state has been reached if there are no targets left
    if len(all_units[target_char]) == 0:
        # Outcome # 5 there are no targets left
        return UnitTurnOutcome.NO_TARGETS_LEFT, None, None

    adj_open_sq_locations = dict()
    adj_attackable_targets = list()

    # Consider all squares adjacent to any of the targets
    for the_location in get_adjacent_squares(all_units[target_char]):

        # if the_location not in current_state:
        #     continue
        # elif current_state[the_location] == '.':
        #     # Since it's an adjacent open square, look up its length later
        #     adj_open_sq_locations[the_location] = None

        if the_location not in current_state:
            # Since it's an adjacent open square, look up its length later
            adj_open_sq_locations[the_location] = None

        elif current_state[the_location] == '#':
            continue

    # See if any adjacent square to position is a target
    for adjacent_location in get_adjacent_squares([position_player]):
        # elif current_state[the_location][0] == target_char:
        #     # It's a target that is adjacent to the attacking unit
        if adjacent_location not in current_state:
            continue
        # if current_state[adjacent_location] == '.':
        if current_state[adjacent_location] == '#':
            continue
        # if current_state[adjacent_location][0] == target_char:
        if current_state[adjacent_location]['char'] == target_char:
            adj_attackable_targets.append(adjacent_location)

    if len(adj_attackable_targets) > 0:
        # Attacks a target (if > 1, it's chosen based on reading order)
        position_target = first__reading_order(adj_attackable_targets)
        target_new_hp = current_state[position_target]['hit_points'] - current_state[position_player]['attack_power']
        if target_new_hp > 0:
            # Outcome # 1:  target attacked and remains alive
            return UnitTurnOutcome.TARGET_ATTACKED_ALIVE, position_target, {'char': target_char, 'hit_points': target_new_hp, 'attack_power': current_state[position_target]['attack_power']}
        else:
            # Outcome # 2:  target attacked and killed off
            # return UnitTurnOutcome.TARGET_KILLED, position_target, '.'
            return UnitTurnOutcome.TARGET_KILLED, position_target
        
   
    elif len(adj_open_sq_locations) > 0:
        # Determine which reachable adj_open_sq_locations (if any) are closest
        # If more than one, select based on reading order, and return
        # If one, select it and return
        # If zero, keep going

        # 
        next_positions = {position_player}
        prior_positions = set()
        current_positions = set()
        step_count = 0
        nearest_open_squares =  set()
        while True:
            step_count += 1
            prior_positions.update(current_positions)
            current_positions = next_positions
            # Get all four adjacent squares
            next_positions = get_adjacent_squares(next_positions)
            # Eliminate all adjacent squares that have been visited previously
            next_positions = next_positions.difference(current_positions).difference(prior_positions)
            ### Disregard either '#' or the other unit type
            # next_positions = {
            #     x
            #     for x in next_positions
            #     if x in current_state  # exclude '#'
            #     and current_state[x] == '.'  # include only open spaces
            # }

            # Only consider open squares (positions not in current_state)
            next_positions = {
                x
                for x in next_positions
                if x not in current_state
            }

            if len(next_positions) == 0:
                # Outcome # 4: nothing happened
                return UnitTurnOutcome.NOTHING_HAPPENED, None, None
        
            # If any next_positions intersect with the known adjacent open square locations
            intersection_set = set(adj_open_sq_locations.keys()).intersection(next_positions)
            if len(intersection_set) > 0:
                pass
                
                return UnitTurnOutcome.CURRENT_UNIT_MOVED, position_player, first__reading_order(list(intersection_set))
                # REALLY .... TAKE A STEP IN THAT DIRECTION .... Outcome # 3

# first__reading_order(position_iterable)



def get_all_units(current_state):
    # all_units = {'E': list(), 'G': list(), '.': list()}
    all_units = {'E': list(), 'G': list(), '#': list()}
    for k,v in current_state.items():
        if type(v) == dict:
            all_units[v['char']].append(k)
        # elif v == '.':
        elif v == '#':
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
            # if current_value == '.':
            if current_value == '#':
                continue


            else:


                # Identify targets, and their distances
                current_value = current_state[position]
                # target_unit = current_value[0]
                target_unit = current_value['char']
                target_char = 'G' if target_unit == 'E' else 'E'


                # target_position, target_endstate = unit_turn(position, current_state)
                # There are five possible outcomes:  
                # (1) a target was attacked but not killed, 
                # (2) a target was attacked and killed off, 
                # (3) the current unit was moved
                # (4) nothing happened
                # (5) there are no targets left

                # target_position, target_endstate = unit_turn(position, target_char, all_units, current_state)
                unit_flag_outcome_flag, param1, param2 = unit_turn(position, target_char, all_units, current_state)

                # Covers outcome 5:  there are no targets left
                if unit_flag_outcome_flag == UnitTurnOutcome.NO_TARGETS_LEFT:
                    return next_state, False
                
                # Covers outcome 4:  nothing happened
                elif unit_flag_outcome_flag == UnitTurnOutcome.NOTHING_HAPPENED:
                    pass

                # Covers outcome 1:  target attacked and its state changed
                elif unit_flag_outcome_flag == UnitTurnOutcome.TARGET_ATTACKED_ALIVE:
                    next_state[param1] = param2
                # Covers outcome 2:  target attacked and killed off
                elif unit_flag_outcome_flag == UnitTurnOutcome.TARGET_KILLED:
                    # Remove the target .... it's now an open square
                    # next_state[param1] = '.'
                    next_state.pop(param1)
                
                # Covers outcome 3:  the current unit is moved
                else:
                    next_state[param2] = current_state[param1]
                    # next_state[param1] = '.'
                    # next_state.pop(param1)

                # FILL_IN_HERE___PROCESS_THAT_UNIT
    
    # If complete
    # next_state['NUM_COLS'] = current_state['NUM_COLS']
    # next_state['NUM_ROWS'] = current_state['NUM_ROWS']
    next_state['ROUND_NUMBER'] += 1
    # CHANGE THE BELOW False to True, when ready to do so
    return next_state, False


def display(current_state):
    print('#' * (current_state['NUM_COLS'] + 2))
    for row_number in range(current_state['NUM_ROWS']):
        unit_information = ''
        print('#', end = '')
        for col_number in range(current_state['NUM_COLS']):
            position = col_number + row_number * 1j
            if position not in current_state:
                # print('#', end = '')
                print('.', end = '')
            else:
                # if type(current_state[position]) == list:
                if type(current_state[position]) == dict:
                    # print(current_state[position][0], end = '')
                    print(current_state[position]['char'], end = '')
                    # unit_information += current_state[position]['char']
                    unit_information += f"{current_state[position]['char']}({current_state[position]['hit_points']}) "
                else:
                    print(current_state[position], end = '')
        print('#  ', end = '')
        print(unit_information)
    print('#' * (current_state['NUM_COLS'] + 2))


def get_final_state(current_state):
    keep_going = True
    while keep_going:
        current_state, keep_going = do_a_round(current_state)
        # if TESTING and keep_going:
        display(current_state)
    return current_state


def solve_problem(input_filename):
    initial_state = get_initial_state(input_filename)
    final_state = get_final_state(initial_state)


solve_problem('input_sample0.txt')

def test_first__reading_order():
    assert first__reading_order([3+2j, 3+3j, 4+2j, 4+3j]) == 3+2j
    assert first__reading_order([3+3j, 4+2j, 4+3j, 3+2j ]) == 3+2j
    assert first__reading_order([1+5j, 5+1j]) == 5+1j
    assert first__reading_order([1+5j, 5+5j]) == 1+5j

