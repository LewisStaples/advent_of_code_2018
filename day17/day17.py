#!/usr/bin/env python3

# adventOfCode 2018 day 17
# https://adventofcode.com/2018/day/17


def get_initial_state(input_filename):
    clay_coords = set()

    margins = {
        'min_x': float('inf'),
        'max_x': float('-inf'),
        'min_y': float('inf'),
        'max_y': float('-inf'),
    }

    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            singleton_str, range_str = in_string.rstrip().split(', ')

            const_var_str = singleton_str[0]
            const_var = int(singleton_str[2:])
            globals()[const_var_str] = const_var
            
            loop_var_str = range_str[0]
            loop_lower, loop_upper = range_str.split('=')[1].split('..')
            for loop_var in range(int(loop_lower), int(loop_upper) + 1):
                globals()[loop_var_str] = loop_var
                clay_coords.add((x,y))

                margins['min_x'] = min(margins['min_x'], x)
                margins['max_x'] = max(margins['max_x'], x)
                margins['min_y'] = min(margins['min_y'], y)
                margins['max_y'] = max(margins['max_y'], y)

    return clay_coords, margins

def display(clay_coords, water_coords, margins):
    if len(clay_coords) < 1:
        # There is nothing to display
        return
    
    for y in range(margins['max_y'] + 1):
        if y == margins['min_y']:
            print('---- ', end= '')
        else:
            print('     ', end= '')
        for x in range(margins['min_x'], margins['max_x'] + 1):
            if (x,y) in clay_coords:
                print('#', end = '')
            elif (x,y) in water_coords:
                print('W', end = '')
            else:
                print('.', end = '')
        if y == margins['min_y']:
            print(' ----')
        else:
            print('     ')
    print()


def vertical_drop(position_in):
    return (position_in[0], position_in[1] + 1)

def get_horizontal_slice(current_position, clay_coords, water_coords, water_positions, margins):
    # new_water_positions = list()
    orig_len_water_positions = len(water_positions) 
    occupied_coords = clay_coords | water_coords

    # Expand the horizontal slice to the left
    new_position = current_position
    while True:
        new_position = (new_position[0] - 1, new_position[1])
        if new_position in clay_coords:
            break
        water_coords.add(new_position)
        # Detect any spill-over
        if (new_position[0], new_position[1] + 1) not in occupied_coords:
            water_positions.append(new_position)
            break

    # Expand the horizontal slice to the right
    new_position = current_position
    while True:
        new_position = (new_position[0] + 1, new_position[1])
        if new_position in clay_coords:
            break
        water_coords.add(new_position)
        # Detect any spill-over
        if (new_position[0], new_position[1] + 1) not in occupied_coords:
            water_positions.append(new_position)
            break

    # If expansion in either direction has led to spill-over,
    if len(water_positions) > orig_len_water_positions:

        # Remove from water positions
        #     The element at index orig_len_water_positions
        #     Plus all elements before that that are immediately above it
        #     Because they have already been accounted for

        pass

    # if len(new_water_positions) > 0:
    #     water_positions = new_water_positions
        


def solve_problem(input_filename):
    # Initial State
    clay_coords, margins = get_initial_state(input_filename)
    water_coords = set()
    display(clay_coords, water_coords, margins)
    
    # Virtual value to start things off
    water_positions = [(500, -1)]

    while True:
        # If possible, the water will go down
        # try:
        vertical_drop_position = vertical_drop(water_positions[-1])
            # vertical_drop_position = vertical_drop(water_positions.pop())
        # except IndexError:
            # return
        if vertical_drop_position not in clay_coords:
            if vertical_drop_position not in water_coords:
                if vertical_drop_position[1] <= margins['max_y']:
                    # water_positions.pop()
                    # if vertical_drop_position not in water_positions:
                    water_positions.append(vertical_drop_position)
                    water_coords.add(vertical_drop_position)
                    continue
            # else:

                else:
                    # water_positions.pop()
                    # continue
                    break

            # water_positions.pop()
            # continue
        # If the water cannot go down, the water will move horizontally
        current_position = water_positions.pop()
        get_horizontal_slice(current_position, clay_coords, water_coords, water_positions, margins)
        display(clay_coords, water_coords, margins)
        # break

    

    display(clay_coords, water_coords, margins)
    return len(water_coords)



water_tile_count = solve_problem('input_sample0.txt')
print(f'The final result is: {water_tile_count}\n')




# def test_sample_0():
#     solve_problem('input_sample0.txt')





