#!/usr/bin/env python3

# adventOfCode 2018 day 18
# https://adventofcode.com/2018/day/18


def get_input(input_filename):
    lumber_collection_area = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    print(f'"." is Open Ground\n"|" is Trees\n"#" is a lumberyard\n')

    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            if len(in_string) < 15:
                print(in_string)
            lumber_collection_area.append(list(in_string))
    print()
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
        if adj_col < 0 | adj_row < 0:
            continue
        acre_type = lca[adj_row][adj_col]
        # if row_number + auv[1] < 0:
        #     continue
        # if col_number + auv[0] < 0:
        #     continue
        # acre_type = lca[row_number + auv[1]][col_number + auv[0]]
        match acre_type:
            case '.': 
                ret_val['open_ground'] += 1
            case '|':
                ret_val['trees'] += 1
            case '#':
                ret_val['lumberyard'] += 1
    print(f'get_adjacents Return value: {ret_val}')
    return ret_val


def solve_problem(input_filename):
    lca_pair = get_lca_pair(input_filename)
    for minutes_passed in range(1, 11):
        # Demonstration only ... actual logic is more complicated
        for row_number, (new_row, old_row) in enumerate(zip(lca_pair[minutes_passed % 2], lca_pair[(minutes_passed - 1) % 2])):
            new_row.clear()
            for column_number, old_ele in enumerate(old_row):
                new_row.append('$')


solve_problem('input_sample0.txt')


def test__get_adjacents():
    lca = get_input('input_sample0.txt')
    assert get_adjacents(lca, 0, 0) == {
        'lumberyard': 1,
        'trees': 0,
        'open_ground': 2,
    }
