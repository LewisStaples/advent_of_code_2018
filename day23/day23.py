#!/usr/bin/env python3

# adventOfCode 2018 day 23
# https://adventofcode.com/2018/day/23


def get_input_DSs(input_filename):
    pos_list = list()
    r_list = list()

    # Reading input
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()

            # Input line into data structures
            left_str, r_str = in_string.split(', r=')
            pos_str = left_str[5:-1].split(',')
            # print(f'{in_string}   pos: {pos_str}   r: {r_str}')
            r_list.append(int(r_str))

            pos = tuple([
                int(x)
                for x in pos_str
            ])
            print(f'{in_string}   pos: {pos}   r: {r_str}')
            pos_list.append(pos)
    return r_list, pos_list


def find_maximum(r_list, pos_list):
    r_max = max(r_list)
    index__r_max = r_list.index(r_max)
    # print(f'Maximum r: {r_max}, Associated POS: {pos_list[index__r_max]}')
    # print()
    return r_max, pos_list[index__r_max]


def manhattan_distance(pos_one, pos_two):
    # return 42
    ret_val = 0
    pos_pair = zip(pos_one, pos_two)
    for ele1, ele2 in pos_pair:
        ret_val += abs(ele1 - ele2)
    return ret_val


def in_range(strongest_nanobot, pos_val, the_range):
    return manhattan_distance(strongest_nanobot, pos_val) <= the_range

def get_nanobot_count_within_range(pos_list, the_range, strongest_nanobot):
    ret_val = 0

    for pos_val in pos_list:
        if in_range(strongest_nanobot, pos_val, the_range):
            ret_val += 1
    return ret_val


def solve_part_one(input_filename):
    r_list, pos_list = get_input_DSs(input_filename)
    the_range, strongest_nanobot = find_maximum(r_list, pos_list)
    nanobot_count_within_range = get_nanobot_count_within_range(pos_list, the_range, strongest_nanobot)

    print(f'The answer to part one is {nanobot_count_within_range}\n')

    # Calculate Manhattan distances for each pos from the largest r's pos
    # If Manhattan distance is <= largest r, then this nanobot is in range.
    # Otherwise, it is not.
    
def solve_part_two(input_filename):
    r_list, pos_list = get_input_DSs(input_filename)
    # Brute force looks like it will work on the example, but not on the graded problem.
    # Instead .... Consider all spheres and then find all intersections between the spheres.
    # Label the shapes cut by these intersections as constant number of chatbots are in range.
    #
    #
    


solve_part_one('input_sample0.txt')
solve_part_two('input_sample1.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')
