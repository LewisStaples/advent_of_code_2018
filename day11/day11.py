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


def get_sum(fuel_cell_grid, dimension_in, x_in, y_in):
    sum = 0
    for x in range(x_in, x_in + dimension_in):
        for y in range(y_in, y_in + dimension_in):
            try:
                sum += fuel_cell_grid[x][y]
            except IndexError:
                dummy = 123
    return sum

def get_answers(fuel_cell_grid):
    best_seen = {
        'highest_sum': float('-inf'),
        'x': None,
        'y': None,
        'dimension': None,
    }

    # USING THE BELOW LINE TAKES TOO LONG ....
    # for dimension in range(1, 301):
    
    for dimension in range(3, 4):
        for x in range(0, 301 - dimension):
            for y in range(0, 301 - dimension):
                this_sum = get_sum(fuel_cell_grid, dimension, x, y)
                if this_sum > best_seen['highest_sum']:
                    best_seen['highest_sum'] = this_sum
                    best_seen['x'] = x
                    best_seen['y'] = y
                    best_seen['dimension'] = dimension

    return f'{best_seen["x"]},{best_seen["y"]},{best_seen["dimension"]}' , 'not-yet-solved'
    
serial_number = get_serial_number('input.txt')
fuel_cell_grid = get_grid(serial_number)

answer_part1 , answer_part2 = get_answers(fuel_cell_grid)
print(f'The answer to part 1 (A) is: {answer_part1}')
print(f'The answer to part 2 (B) is: {answer_part2}')

