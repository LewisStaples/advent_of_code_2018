#!/usr/bin/env python3

# adventOfCode 20xy day 6
# https://adventofcode.com/20xy/day/6


# import numpy as np

# key is the point itself
# value id dict with:
#   which group of points this point is in (index in input file)
#   
# value is dict
all_points = dict()
tenative_new_points = dict()

def get_input(input_filename):
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for group_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            x,y = in_string.split(', ')
            x,y = (int(z) for z in (x,y))
            all_points[(x,y)] = {'group_number': group_number, 'manh_dist': 0}
    return all_points

def get_outer_box(all_points):
    ret_val = {
        'x_min': float('inf'),
        'x_max': float('-inf'),
        'y_min': float('inf'),
        'y_max': float('-inf'),
    }
    for x,y in all_points:
        ret_val['x_min'] = min(ret_val['x_min'], x)
        ret_val['x_max'] = max(ret_val['x_max'], x)
        ret_val['y_min'] = min(ret_val['y_min'], y)
        ret_val['y_max'] = max(ret_val['y_max'], y)
    return ret_val

def extend_til_shown_infinite(all_points, outer_box):
    manh_dist = 0
    while True:
        set_pts = {k for k,v in all_points.items() if v['manh_dist'] == manh_dist}
        # if all set_pts outside outer_box, return set_pts
        flag = True
        for pt in set_pts:
            if pt[0] <= outer_box['x_max']:
                if pt[0] >= outer_box['x_min']:
                    if pt[1] <= outer_box['y_max']:
                        if pt[1] >= outer_box['y_min']:
                            flag = False
        if flag:
            return set_pts

        manh_dist += 1

        for pt in set_pts:
            # find points one step away
            for direction in [[0,-1],[0,1],[1,0],[-1,0]]:
                new_pt = (
                    pt[0] + direction[0],
                    pt[1] + direction[1]
                )
            if new_pt in all_points:
                if all_points[new_pt]['manh_dist'] == manh_dist:
                    all_points[new_pt]['group_number'] = None
                else:
                    assert(all_points[new_pt]['manh_dist'] < manh_dist)
            else:
                all_points[new_pt] = {'group_number': all_points[pt]['group_number'], 'manh_dist': manh_dist}
        # break

def solve_problem(input_filename):
    all_points = get_input(input_filename)
    outer_box = get_outer_box(all_points)
    last_pts = extend_til_shown_infinite(all_points, outer_box)

    dummy = 123

solve_problem('input_sample0.txt')


    