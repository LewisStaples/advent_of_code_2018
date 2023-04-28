#!/usr/bin/env python3

# adventOfCode 2018 day 22
# https://adventofcode.com/2018/day/22


import enum
import heapq
import numpy as np


DIRECTIONS = [
    np.array([0,1]),
    np.array([0,-1]),
    np.array([1,0]),
    np.array([-1,0]),
]

class Equipment(enum.Enum):
    TORCH = 0
    CLIMBING_GEAR = 1
    NEITHER = 2


def get_input(input_filename):
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            var_name, var_value = in_string.split(': ')

            if var_name == 'depth':
                depth = int(var_value)
            elif var_name == 'target':
                str_list = var_value.split(',')
                target = tuple([
                    int(ele)
                    for ele in str_list
                ])
    print()
    return depth, target


def get_erosion_level(geologic_index, depth):
    return (geologic_index + depth) % 20183


def get_regional_geologic_indices(depth, target):
    # This returns a list of lists of integers.
    # Note that the indices are [y][x], which supports printing on the
    # screen with x horizontal and y vertical.
    regional_geologic_indices = list()
    MAX_HEIGHT = max(16, target[1] + 1)
    MAX_LENGTH = max(16, target[0] + 1)
    
    # Top row (height == 0)
    regional_geologic_indices.append(list())
    for length in range(MAX_LENGTH):
        regional_geologic_indices[-1].append(16807 * length)

    # Remaining rows
    for height in range(1, MAX_HEIGHT):
        regional_geologic_indices.append(list())
        regional_geologic_indices[-1].append(48271 * height)
        for length in range(1, MAX_LENGTH):
            regional_geologic_indices[-1].append(
                get_erosion_level(regional_geologic_indices[-1][length - 1], depth)
                * get_erosion_level(regional_geologic_indices[-2][length], depth)
            )
            if (length, height) == target:
                # Set target's geologic index to zero
                regional_geologic_indices[-1][-1] = 0
    return regional_geologic_indices


def display(regional_geologic_indices, target, depth):
    if len(regional_geologic_indices) > 20:
        # Too much data to print on screen !
        return
    for row_num, row in enumerate(regional_geologic_indices):
        for col_num, field in enumerate(row):
            # Print mouth character
            if (col_num, row_num) == (0,0):
                print('M', end = '')
                continue
            # Print target character
            if (col_num, row_num) == target:
                print('T', end = '')
                continue
            
            # Lookup geologic index, calculate erosion level, calculate mod 3 and then match 0,1,2
            match get_erosion_level(regional_geologic_indices[row_num][col_num], depth) % 3:
                # Rocky
                case 0:
                    print('.', end = '')
                # Wet
                case 1:
                    print('=', end = '')
                # Narrow
                case 2:
                    print('|', end = '')
        print()
    print()


def get_total_risk_level(regional_geologic_indices, target, depth):
    ret_val = 0
    for row_num in range(target[1] + 1):
        for col_num in range(target[0] + 1):
            ret_val += get_erosion_level(regional_geologic_indices[row_num][col_num], depth) % 3

    return ret_val


def solve_problem(input_filename):
    # Solving part one
    depth, target = get_input(input_filename)

    regional_geologic_indices = get_regional_geologic_indices(depth, target)
    display(regional_geologic_indices, target, depth)
    total_risk_level = get_total_risk_level(regional_geologic_indices, target, depth)
    print(f'The total risk level (the answer to part one) is: {total_risk_level}\n')

    # Clearing out variables that are no longer needed
    del input_filename, total_risk_level

    # Solving part two
    arrival_times__by_region = dict()
    pq = []
    heapq.heappush(pq, [0, np.array([0,0]), Equipment.TORCH])
    while True:
        # Pull a new data point off of the queue
        try:
            arrival_time, the_region, the_equipment = heapq.heappop(pq)
        except ValueError:
            dummy = 123
        the_region_tuple = tuple(the_region)
        if the_region_tuple not in arrival_times__by_region:
            arrival_times__by_region[the_region_tuple] = {
                Equipment.TORCH: arrival_time + 7,
                Equipment.CLIMBING_GEAR: arrival_time + 7,
                Equipment.NEITHER: arrival_time + 7,
            }
        arrival_times__by_region[the_region_tuple][the_equipment] = min(arrival_time, arrival_times__by_region[the_region_tuple][the_equipment])

        # If appropriate, add new data points to the queue
        # target_nparray = np.array(list(target))
        for vector in DIRECTIONS:
            new_region = the_region + vector
            new_region_tuple = tuple(new_region)
            if new_region[0] < 0 or new_region[1] < 0:
                # The regions with negative X or Y are solid rock and cannot be traversed
                continue
            for the_equipment in Equipment:
                new_arrival_time = 1 + arrival_times__by_region[the_region_tuple][the_equipment]
                # break
            # break
        # break
    
                # Working on logic (commented out, below) to add to pq


                # if new_region_tuple not in arrival_times__by_region or arrival_times__by_region[new_region_tuple][the_equipment] > new_arrival_time:

                flag = False
                if new_region_tuple not in arrival_times__by_region:
                    flag = True
                elif arrival_times__by_region[new_region_tuple][the_equipment] > new_arrival_time:
                    flag = True
                # if [new_arrival_time, new_region, the_equipment] in pq:
                    # flag = False
                if flag:
                    try:
                        heapq.heappush(pq, [new_arrival_time, new_region, the_equipment])
                    except ValueError:
                        dummy = 123

        dummy = 123

        # STOP CONDITION ...
        # If the target has been found
        if target in arrival_times__by_region:
            target_arrival = min(arrival_times__by_region[target])
            # if the smallest arrival time associated with the target is smaller than the smallest arrival_time in pq
            if target_arrival < pq[0][0]:
                break



solve_problem('input_sample0.txt')

def test_0_0 ():
    assert get_regional_geologic_indices(510, (10,10))[0][0] == 0
    assert get_erosion_level(0, 510) == 510

def test_1_0 ():
    assert get_regional_geologic_indices(510, (10,10))[0][1] == 16807
    assert get_erosion_level(16807, 510) == 17317

def test_0_1 ():
    assert get_regional_geologic_indices(510, (10,10))[1][0] == 48271
    assert get_erosion_level(48271, 510) == 8415

def test_1_1 ():
    assert get_regional_geologic_indices(510, (10,10))[1][1] == 145722555
    assert get_erosion_level(145722555, 510) == 1805

def test_10_10 ():
    assert get_regional_geologic_indices(510, (10,10))[10][10] == 0
    assert get_erosion_level(0, 510) == 510
