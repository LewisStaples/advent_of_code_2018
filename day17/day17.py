#!/usr/bin/env python3

# adventOfCode 2018 day 17
# https://adventofcode.com/2018/day/17


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_clay_coords(input_filename):
    clay_coords = set()
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
    return clay_coords

def display(clay_coords, water_coords):
    if len(clay_coords) < 1:
        # There is nothing to display
        return
    
    margins = {
        'min_x': float('inf'),
        'max_x': float('-inf'),
        'max_y': float('-inf'),
    }
    for clay_coord in clay_coords:
        margins['min_x'] = min(margins['min_x'], clay_coord[0])
        margins['max_x'] = max(margins['max_x'], clay_coord[0])
        margins['max_y'] = max(margins['max_y'], clay_coord[1])
    for water_coord in water_coords:
        margins['min_x'] = min(margins['min_x'], water_coord[0])
        margins['max_x'] = max(margins['max_x'], water_coord[0])
        margins['max_y'] = max(margins['max_y'], water_coord[1])

    # Add a margin of 1, and add more to maxes for the for loop
    margins['min_x'] -= 1
    margins['max_x'] += 2
    margins['max_y'] += 2

    for y in range(margins['max_y']):
        for x in range(margins['min_x'], margins['max_x']):
            if (x,y) in clay_coords:
                print('#', end = '')
            elif (x,y) in water_coords:
                print('~', end = '')
            else:
                print('.', end = '')
        print()


def solve_problem(input_filename):
    clay_coords = get_clay_coords(input_filename)
    water_coords = set()
    display(clay_coords, water_coords)



solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')





