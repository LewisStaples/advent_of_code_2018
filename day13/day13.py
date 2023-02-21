#!/usr/bin/env python3

# adventOfCode 2018 day 13
# https://adventofcode.com/2018/day/13


import numpy as np
import copy
import sys


DIRECTIONS = {
    '<': np.array([-1, 0]),
    '^': np.array([ 0,-1]),
    '>': np.array([+1, 0]),
    'v': np.array([ 0,+1]),
}

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
    timestamp = 0
    while True:
        timestamp += 1
        # Take a new step forward in time
        # Compose a new list of all possible states of where carts could be at the end of this clock tick
        new_cart_collection_list = list()
        # Loop through each of all possible states of where carts could be at the start of this clock tick
        # (old_cart_collection is one of these states of where carts could be at the start of this clock tick)
        for old_cart_collection in old_cart_collection_list:
            # Compose a new list for one possible state of where carts could be at the end of this clock tick
            new_cart_collection = list()
            # For starting position of one cart in one possible state of all carts
            for old_cart in old_cart_collection:
                old_track_ch, old_location = old_cart
                old_location = old_cart[1]
                old_track_ch = tracks[tuple(old_location)]
                if old_track_ch == '+':

                    #
                    # NEEDED TO TEST IN THE FUTURE !!!!
                    #

                    for new_cart_ch, step in DIRECTIONS:
                        # copy.deepcopy(old_cart_collection).append(['<',old_location + step])
                        if new_cart_ch != '<':
                            new_cart_collection = copy.deepcopy(old_cart_collection)
                        else:
                            new_cart_collection = old_cart_collection
                        
                        #
                        # NEED TO ADD, AND THEN TEST ... Remove old cart from new_cart_collection
                        #

                        new_cart_collection.append([new_cart_ch,old_location + step])
                        dummy = 123
                        new_cart_collection_list.append(new_cart_collection)

                        # Skip below code for updating new_cart_collection
                        continue

                # Implement later .....
                
                new_cart = copy.deepcopy(old_cart)
                if old_track_ch in ['\\','/']:
                    # Modify cart character ... 1:1 relationship
                    # new_cart = None
                    
                    pass
                else:
                    assert(old_track_ch in ['|','-'])
                    dummy = 123
                
                # Move cart, based on new_cart
                new_cart[1] += DIRECTIONS[new_cart[0]]
                # new_cart_collection_list.append(old_cart_collection)
                new_cart_collection.append(new_cart)

            new_cart_collection_list.append(new_cart_collection)

        display(tracks, new_cart_collection_list, timestamp)
        old_cart_collection_list = new_cart_collection_list
        # break
    return ''



def print_cart_if_here(cart_collection, location):
    for cart in cart_collection:
        if tuple(location) == tuple(cart[1]):
            print(cart[0], end='')
            return True
    return False



def display(tracks, cart_collection_list, timestamp):
    '''
    This will only display the tracks and carts with
        x_values between 0 and X_MAX
        y_values between 0 and Y_MAX

        (That should display everything for the given sample data,
        but it will not error out if run with the graded problem)
    '''


    X_MAX = 20
    Y_MAX = 10
    print(f'ALL POSSIBLE LOCATIONS OF CARTS AT TIMESTAMP {timestamp}:')
    for cart_collection in cart_collection_list:
        print()
        for y in range(Y_MAX + 1):
            for x in range(X_MAX + 1):
                location = np.array([x,y])
                # If there is a cart at (x,y), print it
                if print_cart_if_here(cart_collection, location):
                    continue
                # Since there isn't a cart at (x,y)
                else:
                    if (x,y) in tracks:
                        # If there is a track at (x,y), then print it
                        print(tracks[(x,y)], end='')
                    else:
                        # Since there is neither a cart nor track at (x,y), print a space
                        print(' ', end='')
            print()

    # PREVENTING INFINITE LOOP, FOR NOW .....
    if timestamp == 1:
        sys.exit(f'PLANNED EXIT FOR TIMESTAMP {timestamp}')


def solve_problem(input_filename):
    tracks, cart_collection_list = get_input_line(input_filename)
    display(tracks, cart_collection_list, 0)
    print(f'Answer to A/1: {get_first_crash_location(tracks, cart_collection_list)}')
    dummy = 123

# solve_problem('input_sample0.txt')

solve_problem('input_sample1.txt')

# solve_problem('input.txt')





