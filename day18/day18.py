#!/usr/bin/env python3

# adventOfCode 2018 day 18
# https://adventofcode.com/2018/day/18

import collections

def display(lca):
    if len(lca) > 15:
        return
    for row in lca:
        print(''.join(row))
    print()


def get_input(input_filename):
    lumber_collection_area = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    print(f'"." is Open Ground\n"|" is Trees\n"#" is a lumberyard\n')

    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            lumber_collection_area.append(list(in_string))
    print('Initial LCA status:')
    display(lumber_collection_area)
    return lumber_collection_area
    

def get_lca_pair(input_filename):
    lca_pair = [None, None]
    lca_pair[0] = get_input(input_filename)
    lca_pair[1] = [
        list()
        for row in lca_pair[0]
    ]
    return lca_pair


def get_adjacents(lca, row_number, col_number):
    ADJACENT_UNIT_VECTORS = [
        (-1,0),
        (1,0),
        (-1,1),
        (1,1),
        (0,1),
        (-1,-1),
        (1,-1),
        (0,-1),
    ]

    ret_val = {
        'open_ground': 0,
        'trees': 0,
        'lumberyard': 0
    }

    for auv in ADJACENT_UNIT_VECTORS:
        adj_row = row_number + auv[1]
        adj_col = col_number + auv[0]
        # Protect against indices less than zero
        if (adj_col < 0) | (adj_row < 0):
            continue
        try:
            acre_type = lca[adj_row][adj_col]
        # Protect against indices that are greater than maximum for that index
        except IndexError:
            continue
        match acre_type:
            case '.': 
                ret_val['open_ground'] += 1
            case '|':
                ret_val['trees'] += 1
            case '#':
                ret_val['lumberyard'] += 1
    return ret_val


def get_total_resource_value(lca_pair, minutes_passed):
    acre_type_count = {
        'open_ground': 0,
        'trees': 0,
        'lumberyard': 0
    }

    for row in lca_pair[minutes_passed % 2]:
        for acre_char in row:
            match acre_char:
                case '.':
                    acre_type_count['open_ground'] += 1
                case '|':
                    acre_type_count['trees'] += 1
                case '#':
                    acre_type_count['lumberyard'] += 1

    return acre_type_count['trees'] * acre_type_count['lumberyard']


def solve_problem(input_filename):
    trv_deque = collections.deque([], 100)
    lca_pair = get_lca_pair(input_filename)
    for minutes_passed in range(1, 1001):
        for row_number, (new_row, old_row) in enumerate(zip(lca_pair[minutes_passed % 2], lca_pair[(minutes_passed - 1) % 2])):
            new_row.clear()
            for column_number, old_ele in enumerate(old_row):
                new_ele = old_ele
                adjacents = get_adjacents(lca_pair[(minutes_passed - 1) % 2], row_number, column_number)
                if old_ele == '.':  # open ground
                    if adjacents['trees'] >= 3:
                        new_ele = '|'  # now it's trees:

                if old_ele == '|': # trees
                    if adjacents['lumberyard'] >= 3:
                        new_ele = '#' # now it's a lumberyard

                if old_ele == '#': # lumberyard
                    if (adjacents['lumberyard'] < 1) | (adjacents['trees'] < 1):
                        new_ele = '.' # now it's open ground
                new_row.append(new_ele)
        # print(f'Minutes passed: {minutes_passed}')

        trv = get_total_resource_value(lca_pair, minutes_passed)
        # trv_deque.append((minutes_passed, trv))
        # trv_deque.append(trv)
        trv_deque.appendleft(trv)
        # Print out answer to first part of the problem
        if minutes_passed == 10:
            print(f'When minutes passed: {minutes_passed},  Total Resource Value: {trv}' )
            # display(lca_pair[minutes_passed % 2])

    # print(f'The ending total resource value is: {get_total_resource_value(lca_pair, minutes_passed)} \n')

    # for i in range(-1, -11, -1):
    for i in range(27):
        # print(i)
        # popped_ele = trv_deque.pop()
        popped_ele = trv_deque.popleft()
        print(f'Index {i}: First match: {trv_deque.index(popped_ele)}')
        # if popped_ele not in trv_deque:
        #     print('No match')
        #     break
        # if trv_deque[i] no

solve_problem('input.txt')


def test__get_adjacents():
    lca = get_input('input_sample0.txt')
    assert get_adjacents(lca, 0, 0) == {
        'lumberyard': 1,
        'trees': 0,
        'open_ground': 2,
    }
