#!/usr/bin/env python3

# adventOfCode 2018 day 10
# https://adventofcode.com/2018/day/10

from collections import deque


def str_to_list(in_string):
    the_list = list(in_string.split(", "))
    return [int(x) for x in the_list]


def get_input(input_filename):
    positions = list()
    velocities = list()
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            l_string, r_string = in_string.rstrip().split("> velocity=<")
            l_string = l_string[10:]
            r_string = r_string[:-1]
            positions.append(str_to_list(l_string))
            velocities.append(str_to_list(r_string))
    return positions, velocities


def get_bounding_box(positions):
    return_value = {
        "smallest_x": float("inf"),
        "largest_x": float("-inf"),
        "smallest_y": float("inf"),
        "largest_y": float("-inf"),
    }
    for x, y in positions:
        return_value["smallest_x"] = min(return_value["smallest_x"], x)
        return_value["largest_x"] = max(return_value["largest_x"], x)
        return_value["smallest_y"] = min(return_value["smallest_y"], y)
        return_value["largest_y"] = max(return_value["largest_y"], y)
    return return_value


def display(positions, title):
    bounding_box = get_bounding_box(positions)
    print(title)
    for y in range(bounding_box["smallest_y"], bounding_box["largest_y"] + 1):
        for x in range(bounding_box["smallest_x"], bounding_box["largest_x"] + 1):
            if [x, y] in positions:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def bounding_box_area(bounding_box):
    return (bounding_box["largest_x"] - bounding_box["smallest_x"]) + (
        bounding_box["largest_y"] - bounding_box["smallest_y"]
    )


def completed(positions, time_elapsed, last_three_bba):
    """
    This function returns True when the three most recent bounding boxes have
    a local minimum in the middle (at index one)
    """
    bounding_box = get_bounding_box(positions)
    bba = bounding_box_area(bounding_box)
    last_three_bba.append(bba)
    last_three_bba.popleft()
    if last_three_bba[1] < min(last_three_bba[0], last_three_bba[2]):
        return True


def next_step(positions, velocities, step=1):
    ret_val = list()
    for the_index in range(len(positions)):
        ret_val.append(
            [
                positions[the_index][0] + step * velocities[the_index][0],
                positions[the_index][1] + step * velocities[the_index][1],
            ]
        )
    return ret_val


def solve_problem(input_filename):
    positions, velocities = get_input(input_filename)
    time_elapsed = 0
    last_three_bba = deque([float("inf"), float("inf"), float("inf")])
    while True:
        time_elapsed += 1
        positions = next_step(positions, velocities)
        if completed(positions, time_elapsed, last_three_bba):
            break

    positions = next_step(positions, velocities, -1)
    display(positions, f"Message:  from Positions at time {time_elapsed - 1}\n")
    print()


solve_problem("input_sample0.txt")
