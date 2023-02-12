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


def get_sum(fuel_cell_grid, x_in, y_in):
    sum = 0
    for x in range(x_in, x_in + 3):
        for y in range(y_in, y_in + 3):
            sum += fuel_cell_grid[x][y]
    return sum

def get_t_l_coords_largest_3x3_square(fuel_cell_grid):
    best_seen = {
        'highest_sum': float('-inf'),
        'x': None,
        'y': None,
    }
    for x in range(298):
        for y in range(298):
            this_sum = get_sum(fuel_cell_grid, x, y)
            if this_sum > best_seen['highest_sum']:
                best_seen['highest_sum'] = this_sum
                best_seen['x'] = x
                best_seen['y'] = y

    return f'{best_seen["x"]},{best_seen["y"]}'

serial_number = get_serial_number('input.txt')
fuel_cell_grid = get_grid(serial_number)



answer_part1 = get_t_l_coords_largest_3x3_square(fuel_cell_grid)

# print(f'{answer_part1["x"]},{answer_part1["y"]}')
print(f'The answer to part 1 (A) is: {answer_part1}')



