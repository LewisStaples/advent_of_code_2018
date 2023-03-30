#!/usr/bin/env python3

# adventOfCode 2018 day 17
# https://adventofcode.com/2018/day/17


# import numpy as np
# import copy

# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_initial_state(input_filename):
    clay_coords = set()

    margins = {
        'min_x': float('inf'),
        'max_x': float('-inf'),
        'min_y': float('inf'),
        'max_y': float('-inf'),
    }

    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            singleton_str, range_str = in_string.rstrip().split(', ')

            const_var_str = singleton_str[0]
            const_var = int(singleton_str[2:])
            globals()[const_var_str] = const_var
            
            loop_var_str = range_str[0]
            loop_lower, loop_upper = range_str.split('=')[1].split('..')
            for loop_var in range(int(loop_lower), int(loop_upper) + 1):
                globals()[loop_var_str] = loop_var
                clay_coords.add((x,y))

                margins['min_x'] = min(margins['min_x'], x)
                margins['max_x'] = max(margins['max_x'], x)
                margins['min_y'] = min(margins['min_y'], y)
                margins['max_y'] = max(margins['max_y'], y)

    # # Add horizontal margins of 1
    # margins['min_x'] -= 1
    # margins['max_x'] += 1

    # NO .....
    #
    # Add more to margin maxes for the for loop
    # margins['max_x'] += 1
    # margins['max_y'] += 1
    return clay_coords, margins

def display(clay_coords, water_coords, margins):
    if len(clay_coords) < 1:
        # There is nothing to display
        return
    
    for y in range(margins['max_y'] + 1):
        if y == margins['min_y']:
            print('---- ', end= '')
        else:
            print('     ', end= '')
        for x in range(margins['min_x'], margins['max_x'] + 1):
            if (x,y) in clay_coords:
                print('#', end = '')
            elif (x,y) in water_coords:
                print('W', end = '')
            else:
                print('.', end = '')
        if y == margins['min_y']:
            print(' ----')
        else:
            print('     ')
        # print(' ----')
    print()


def vertical_drop(clay_coords, water_coords, margins):
    pass

def new_water_drop(clay_coords, water_coords, margins):
    # new_drop = np.array([500,0])
    new_drop = (500,0)

    # # Vertical drop through sand
    # while True:
    #     newer_drop = (new_drop[0], new_drop[1])
    #     if in clay_coords:
    #         return

    # while (new_drop[0], new_drop[1] + 1) not in clay_coords:

    # while True:
    #     if vertical_drop(clay_coords, water_coords, margins, new_drop):
    #         continue

    # while True:
    #     new_drop = 
    #     # newer_drop = copy.copy(new_drop)
    #     # newer_drop = copy.copy(new_drop)
    #     # newer_drop[0] -= 1
    #     # if new

    #     dummy = 123

    return water_coords

def within_margins(position, margins):
    if position[0] >= margins['min_x']:
        if position[0] <= margins['max_x']:
            if position[1] >= margins['min_y']:
                if position[1] <= margins['max_y']:
                    return True
    return False

def solve_problem(input_filename):
    # Initial State
    clay_coords, margins = get_initial_state(input_filename)
    water_coords = set()
    display(clay_coords, water_coords, margins)
    
    # Virtual value to start things off
    latest_water_position = (500, -1)

    while True:
        new_position = (latest_water_position[0], latest_water_position[1] + 1)
        if new_position in clay_coords:
            display(clay_coords, water_coords, margins)
            return
        else:
            # Only add the water drop if it is within all margins
            if within_margins(new_position, margins):
                water_coords.add(new_position)

        # if new_position in water_coords:
        #     return
        latest_water_position = new_position

    # # Fill with water
    # while True:
    #     position = latest_water__level.pop()
    #     new_position = (position[0], position[1] - 1)
    #     if new_position in clay_coords:
    #         display(clay_coords, water_coords, margins)
    #         return
    #     if new_position in water_coords:
    #         display(clay_coords, water_coords, margins)
    #         return
    #     water_coords.add(new_position)
    #     latest_water__level.add(new_position)
    #     # latest_water__level.add(new_position)



solve_problem('input_sample0.txt')


# def test_sample_0():
#     solve_problem('input_sample0.txt')





