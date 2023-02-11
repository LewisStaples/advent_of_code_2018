#!/usr/bin/env python3

# adventOfCode 2018 day 11
# https://adventofcode.com/2018/day/11

def get_grid(serial_number):
    grid = [ [None] * 300 ] * 300

    for x in range(300):
        for y in range(300):

    # for x in range(21, 24):
    #     for y in range(61, 64):
            grid_value = ( (x + 10) * y + serial_number ) * (x + 10)
            grid[x][y] = ( grid_value % 1000 - grid_value % 100 ) // 100 - 5

            dummy = 123

    return grid

def get_serial_number(input_filename):
    # Reading input from the input file
    # input_filename='input_sample0.txt'
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    
    # Parsing input file   
    serial_number = int(in_string.split('=')[1])

    return serial_number

serial_number = get_serial_number('input_sample1.txt')
fuel_cell_grid = get_grid(serial_number)
dummy = 123


