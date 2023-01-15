#!/usr/bin/env python3

# adventOfCode 20xy day 6
# https://adventofcode.com/20xy/day/6

def get_given_coordinates(input_filename):
    given_coordinates = set() #  dict() # set()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            x,y = in_string.split(', ')
            x,y = (int(z) for z in (x,y))
            given_coordinates.add((x,y))
            # given_coordinates[(x,y)] = True

    return given_coordinates

def get_outer_box(given_coordinates):
    ret_val = {
        'x_min': float('inf'),
        'x_max': float('-inf'),
        'y_min': float('inf'),
        'y_max': float('-inf'),
    }
    for x,y in given_coordinates:
        ret_val['x_min'] = min(ret_val['x_min'], x)
        ret_val['x_max'] = max(ret_val['x_max'], x)
        ret_val['y_min'] = min(ret_val['y_min'], y)
        ret_val['y_max'] = max(ret_val['y_max'], y)
    return ret_val

def manh_dist(init_point, point):
    return abs(init_point[0] - point[0]) + abs(init_point[1] - point[1])

def tot_manh_dist_in_range(given_coordinates, point):
    total_manh_dist = 0
    if len(given_coordinates) == 6:
        max_manh_dist = 31 # ungraded sample input
    elif len(given_coordinates) == 50:
        max_manh_dist = 9999 # graded input
    for init_point in given_coordinates:
        total_manh_dist += manh_dist(init_point, point)
    return total_manh_dist <= max_manh_dist


def get_points_on_box_perimeter(given_coordinates, outer_box):
    ret_val = set() # dict()
    for x in range(outer_box['x_min'], outer_box['x_max'] + 1):
        y = outer_box['y_min']
        if tot_manh_dist_in_range(given_coordinates, (x,y)):
            # ret_val[(x,y)] = True
            ret_val.add((x,y))
        # else:
        #     ret_val[(x,y)] = False
        y = outer_box['y_max']
        if tot_manh_dist_in_range(given_coordinates, (x,y)):
            # ret_val[(x,y)] = True
            ret_val.add((x,y))
        # else:
        #     ret_val[(x,y)] = False
    for y in range(outer_box['y_min'], outer_box['y_max'] + 1):
        x = outer_box['x_min']
        if tot_manh_dist_in_range(given_coordinates, (x,y)):
            # ret_val[(x,y)] = True
            ret_val.add((x,y))
        # else:
        #     ret_val[(x,y)] = False
        x = outer_box['x_max']
        if tot_manh_dist_in_range(given_coordinates, (x,y)):
            # ret_val[(x,y)] = True
            ret_val.add((x,y))
        # else:
        #     ret_val[(x,y)] = False

    return ret_val
def get_points_inside_box_perimeter(given_coordinates, outer_box):
    # ret_val = dict()
    ret_val = set()
    for x in range(outer_box['x_min'] + 1, outer_box['x_max']):
        for y in range(outer_box['y_min'] + 1, outer_box['y_max']):
            if tot_manh_dist_in_range(given_coordinates, (x,y)):
                # ret_val[(x,y)] = True
                ret_val.add((x,y))
            # else:
            #     ret_val[(x,y)] = False
    return ret_val

def solve_problem(input_filename):
    given_coordinates = get_given_coordinates(input_filename)
    outer_box = get_outer_box(given_coordinates)
    points_total_manh_dist_lt_threshold = get_points_on_box_perimeter(given_coordinates, outer_box)
    # if points_total_manh_dist_lt_threshold is None:
    # if True not in points_total_manh_dist_lt_threshold.values():
    if len(points_total_manh_dist_lt_threshold) == 0:
        # Don't need to consider points outside of the box
        points_total_manh_dist_lt_threshold = get_points_inside_box_perimeter(given_coordinates, outer_box)

        print(f'The answer to part B is {len(points_total_manh_dist_lt_threshold)}\n')

solve_problem('input.txt')

