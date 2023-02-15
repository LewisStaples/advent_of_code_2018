#!/usr/bin/env python3

# adventOfCode 2018 day 11
# https://adventofcode.com/2018/day/11


def get_grid(serial_number):
    grid = [[None] * CELL_LENGTH for i in range(CELL_LENGTH)]
    for x in range(CELL_LENGTH):
        for y in range(CELL_LENGTH):
            grid_value = ((x + 10) * y + serial_number) * (x + 10)
            grid[x][y] = (grid_value % 1000 - grid_value % 100) // 100 - 5
    return grid


def get_serial_number(input_filename):
    """
    This function gets the serial number from the input file
    (The problem description indicates that this is the "puzzle input")
    """
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}")
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    # Parsing input file
    serial_number = int(in_string.split("=")[1])
    print(f"The serial number is: {serial_number}\n")
    return serial_number


def get_summed_area_table(input_table):
    """
    The determines the summed area table
    (For an explanation, see below Wikipedia article)
    https://en.wikipedia.org/wiki/Summed-area_table
    """
    # Require that input_table is a list of lists of int
    assert type(input_table) == list
    assert type(input_table[0]) == list
    assert type(input_table[0][0]) == int
    summed_area__table = list()
    for i in range(len(input_table)):
        summed_area__table.append(list())
        for j in range(len(input_table[0])):
            new_value = input_table[i][j]
            if i > 0:
                new_value += summed_area__table[i - 1][j]
            if j > 0:
                new_value += summed_area__table[i][j - 1]
            if (i > 0) and (j > 0):
                new_value -= summed_area__table[i - 1][j - 1]
            summed_area__table[i].append(new_value)
    return summed_area__table


def get_best_square(dimension, sum_area_FCG):
    """
    For a given summed area table that represents a grid of fuel cells ascertain
    which square of cells with the given dimension has the highest sum.
    Return a dict with information about that square.
    """
    best_seen = {
        "highest_sum": float("-inf"),
        "x": None,
        "y": None,
        "dimension": None,
    }
    for x in range(0, CELL_LENGTH - dimension):
        for y in range(0, CELL_LENGTH - dimension):
            this_sum = (
                sum_area_FCG[x][y]
                + sum_area_FCG[x + dimension][y + dimension]
                - sum_area_FCG[x + dimension][y]
                - sum_area_FCG[x][y + dimension]
            )
            if this_sum > best_seen["highest_sum"]:
                best_seen["highest_sum"] = this_sum
                best_seen["x"] = x + 1
                best_seen["y"] = y + 1
                best_seen["dimension"] = dimension
    return best_seen


def get_answers(fuel_cell_grid):
    """
    This function returns a pair of strings with the answers to the A.O.C. problems.
    (Almost all of the logic is passed off to get_best_square)
    """
    # Solving Part 1 / A with the summed area table
    sum_area_FCG = get_summed_area_table(fuel_cell_grid)
    part_one = ",".join(
        [
            f"{v}"
            for (k, v) in get_best_square(3, sum_area_FCG).items()
            if k in ["x", "y"]
        ]
    )
    # Solving Part 2 / B with the summed area table
    best_seen = {
        "highest_sum": float("-inf"),
        "x": None,
        "y": None,
        "dimension": None,
    }
    for dimension in range(1, 301):
        best_seen_this_dim = get_best_square(dimension, sum_area_FCG)
        if best_seen_this_dim["highest_sum"] > best_seen["highest_sum"]:
            best_seen = best_seen_this_dim
    part_two = ",".join(
        [f"{v}" for (k, v) in best_seen.items() if k in ["x", "y", "dimension"]]
    )
    return part_one, part_two


def test__get_summed_area_table():
    """
    This tests function get_summed_area_table

    It uses the example input and output from slide 3 from the below PDF
    https://developer.amd.com/wordpress/media/2012/10/GDC2005_SATEnvironmentReflections.pdf
    """
    init_table = list()
    init_table.append([2, 3, 2, 1])
    init_table.append([3, 0, 1, 2])
    init_table.append([1, 3, 1, 0])
    init_table.append([1, 4, 2, 2])
    s_a_t = get_summed_area_table(init_table)
    assert s_a_t[0] == [2, 5, 7, 8]
    assert s_a_t[1] == [5, 8, 11, 14]
    assert s_a_t[2] == [6, 12, 16, 19]
    assert s_a_t[3] == [7, 17, 23, 28]


CELL_LENGTH = 300
serial_number = get_serial_number("input_sample1.txt")
fuel_cell_grid = get_grid(serial_number)
answer_part1, answer_part2 = get_answers(fuel_cell_grid)
print(f"The answer to input for part 1 (A) is: {answer_part1}")
print(f"The answer to input for part 2 (B) is: {answer_part2}")
print()
