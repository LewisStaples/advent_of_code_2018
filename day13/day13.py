#!/usr/bin/env python3

# adventOfCode 2018 day 13
# https://adventofcode.com/2018/day/13


import numpy as np
import copy


def get_input_line(input_filename):
    tracks = dict()
    carts = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(in_string)
            for col_number, ch in enumerate(in_string):
                if ch in ['v','^']:
                    carts.append([ch,np.array([col_number, row_number])])
                    tracks[(col_number, row_number)]  = '|'
                elif ch in ['<','>']:
                    carts.append([ch,np.array([col_number, row_number])])
                    tracks[(col_number, row_number)] = '-'
                elif ch == ' ':
                    pass
                else:
                    tracks[(col_number, row_number)] = ch
    print()

    return tracks, [carts]


def get_first_crash_location(tracks, old_cart_collection_list):
    while True:
        # Take a new step forward in time
        # Compose a new list of all possible states of where carts could be at the end of this clock tick
        new_cart_collection_list = list()
        # Loop through each of all possible states of where carts could be at the start of this clock tick
        for old_cart_collection in old_cart_collection_list:
            new_cart_collection = old_cart_collection
            # For starting position of one cart in one possible state of all carts
            for old_cart in old_cart_collection:
                old_track_ch, old_location = old_cart
                old_location = old_cart[1]
                old_track_ch = tracks[tuple(old_location)]
                if old_track_ch == '+':
                    # NEEDED FOR NEXT STEP .... ADD SYMBOL (<  >  v  ^)
                    for i, step in enumerate((
                        np.array([0,1]),
                        np.array([0,-1]),
                        np.array([1,0]),
                        np.array([-1,0]),
                    )):
                        # copy.deepcopy(old_cart_collection).append(['<',old_location + step])
                        if i < 3:
                            new_cart_collection = copy.deepcopy(old_cart_collection)
                        new_cart_collection.append(['<',old_location + step])
                        dummy = 123
                        new_cart_collection_list.append(new_cart_collection)

                # Implement later .....
                elif old_track_ch in ['\\','/']:
                    pass
                else:
                    assert(old_track_ch in ['|','-'])
                    pass



        break
    return ''


def solve_problem(input_filename):
    tracks, cart_collection_list = get_input_line(input_filename)
    print(f'Answer to A/1: {get_first_crash_location(tracks, cart_collection_list)}')
    dummy = 123

# solve_problem('input_sample0.txt')

solve_problem('input_sample1.txt')

# solve_problem('input.txt')





