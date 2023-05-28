#!/usr/bin/env python3

# adventOfCode 2018 day 25
# https://adventofcode.com/2018/day/25


import numpy as np
import itertools

def get_three_cube(this_point):
    three_cube = set()
    # print(this_point)
    for dude in itertools.product(range(-3, 4), repeat = 4):
        # print(np.array(dude))
        new_point = this_point + np.array(dude)
        three_cube.add(tuple(new_point))
        # print(new_point)
        # pass
    return three_cube

def get_constellation_count(input_filename):
    constellation_list = [set()]
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            this_point = np.array([int(x) for x in in_string.rstrip().split(',')])
            print(this_point)
            three_cube = get_three_cube(this_point)
            indices_constellation = list()

            for index_constellation, constellation in enumerate(constellation_list):
                if len(constellation.intersection(three_cube)) > 0:
                    indices_constellation.append(index_constellation)
                    break
            print()
    print()

    return 42
    
constellation_count = get_constellation_count('input_sample0.txt')
print(f'The number of constellations is: {constellation_count}')

