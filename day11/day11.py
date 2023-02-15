#!/usr/bin/env python3

# adventOfCode 2018 day 11
# https://adventofcode.com/2018/day/11

def get_grid(serial_number):
    grid = [ [None] * 300 for i in range(300)]

    for x in range(300):
        for y in range(300):
            grid_value = ( (x + 10) * y + serial_number ) * (x + 10)
            grid[x][y] = ( grid_value % 1000 - grid_value % 100 ) // 100 - 5

    return grid

def get_serial_number(input_filename):
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    
    # Parsing input file   
    serial_number = int(in_string.split('=')[1])
    print(f'The serial number is: {serial_number}\n')

    return serial_number


# def get_sum(fuel_cell_grid, dimension_in, x_in, y_in):
#     sum = 0
#     for x in range(x_in, x_in + dimension_in):
#         for y in range(y_in, y_in + dimension_in):
#             try:
#                 sum += fuel_cell_grid[x][y]
#             except IndexError:
#                 dummy = 123
#     return sum

def get_summed_area_table(input_table):
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
                new_value += summed_area__table[i-1][j]
            if j > 0:
                new_value += summed_area__table[i][j-1]
            if (i > 0) and (j > 0):
                new_value -= summed_area__table[i-1][j-1]
            # Modify below to include values to the left and above of it
            # new_value = input_table[i][j]
            # if i > 0:
            #     new_value += summed_area__table[i-1][j]
            summed_area__table[i].append(new_value)
            # print(summed_area__table)
    return summed_area__table

    
def get_answers(fuel_cell_grid):


    # Solving Part 1 / A with the summed area table
    sum_area_FCG = get_summed_area_table(fuel_cell_grid)

    dimension = 3
    best_seen = {
        'highest_sum': float('-inf'),
        'x': None,
        'y': None,
        'dimension': None,
    }
    for x in range(0, 300 - dimension):
        for y in range(0, 300 - dimension):
            this_sum = sum_area_FCG[x][y] + sum_area_FCG[x+dimension][y+dimension] - sum_area_FCG[x+dimension][y] - sum_area_FCG[x][y+dimension]
            if this_sum > best_seen['highest_sum']:
                best_seen['highest_sum'] = this_sum
                best_seen['x'] = x + 1
                best_seen['y'] = y + 1
                best_seen['dimension'] = dimension
    part_one = f'{best_seen["x"]},{best_seen["y"]}'

    # Solving Part 2 / B with the summed area table
    sum_area_FCG = get_summed_area_table(fuel_cell_grid)


    best_seen = {
        'highest_sum': float('-inf'),
        'x': None,
        'y': None,
        'dimension': None,
    }
    for dimension in range(1, 301):
        for x in range(0, 300 - dimension):
            for y in range(0, 300 - dimension):
                this_sum = sum_area_FCG[x][y] + sum_area_FCG[x+dimension][y+dimension] - sum_area_FCG[x+dimension][y] - sum_area_FCG[x][y+dimension]
                if this_sum > best_seen['highest_sum']:
                    best_seen['highest_sum'] = this_sum
                    best_seen['x'] = x + 1
                    best_seen['y'] = y + 1
                    best_seen['dimension'] = dimension
    
    part_two = f'{best_seen["x"]},{best_seen["y"]},{best_seen["dimension"]}'
    return part_one , part_two


def test__get_summed_area_table():
    # Using example from slide 3 on the below PDF
    # https://developer.amd.com/wordpress/media/2012/10/GDC2005_SATEnvironmentReflections.pdf

    init_table = list()
    init_table.append([2, 3, 2, 1])
    init_table.append([3, 0, 1, 2])
    init_table.append([1, 3, 1, 0])
    init_table.append([1, 4, 2, 2])

    # print()
    # display(init_table)

    s_a_t = get_summed_area_table(init_table)
    # display(s_a_t)
    assert s_a_t[0] == [2,5,7,8]
    assert s_a_t[1] == [5,8,11,14]
    assert s_a_t[2] == [6,12,16,19]
    assert s_a_t[3] == [7,17,23,28]

    # print( s_a_t[0] )


serial_number = get_serial_number('input.txt')
fuel_cell_grid = get_grid(serial_number)

answer_part1 , answer_part2 = get_answers(fuel_cell_grid)
print(f'The answer to part 1 (A) is: {answer_part1}')
print(f'The answer to part 2 (B) is: {answer_part2}')

