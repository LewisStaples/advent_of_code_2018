#!/usr/bin/env python3

# adventOfCode 2018 day 16
# https://adventofcode.com/2018/day/16

TEST = False
TEST = True

def get_number_list(in_string):
    in_string = in_string.replace(',', '')
    # Truncate all text to the left of the first digit
    while not in_string[0].isdigit():
        in_string = in_string[1:]
    # Truncate all text to the right of the last digit
    while not in_string[-1].isdigit():
        in_string = in_string[:-1]
    # print(in_string)
    the_number_list = [int(num) for num in in_string.split(' ')]
    return the_number_list
    

def get_final_register_values(register_values, instruction_values):
    # To be implemented later ....
    return -42

def get_count_opcodes_with_result(input_filename):
    # Reading input from the input file
    register_values = None
    instruction_values = None
    opcode_succ_count = 0

    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for line_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            match line_number % 4:
                case 0:
                    if in_string[:7] != 'Before:':
                        break
                    register_values = get_number_list(in_string)
                case 1:
                    instruction_values = get_number_list(in_string)
                case 2:
                    if get_final_register_values(register_values, instruction_values) == get_number_list(in_string):
                        opcode_succ_count += 1
            if TEST:
                print(in_string)

        # Sample test program ... not used in part 1

    print()
    
def solve_problem(input_filename):
    in_string = get_count_opcodes_with_result(input_filename)



solve_problem('input_scenario0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')