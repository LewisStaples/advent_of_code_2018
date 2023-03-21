#!/usr/bin/env python3

# adventOfCode 2018 day 16
# https://adventofcode.com/2018/day/16

TEST = False
TEST = True

import copy

# Storing the name of each operation, followed by the type of operator:  binary, unary, or conditional

ALL_OPCODES = {'addr': 'binary', 'addi': 'binary', 'mulr': 'binary', 'muli':'binary', 
               'banr':'binary', 'bani':'binary', 'borr':'binary', 'bori':'binary',
               }

def get_number_list(in_string):
    in_string = in_string.replace(',', '')
    # Truncate all text to the left of the first digit
    while not in_string[0].isdigit():
        in_string = in_string[1:]
    # Truncate all text to the right of the last digit
    while not in_string[-1].isdigit():
        in_string = in_string[:-1]
    the_number_list = [int(num) for num in in_string.split(' ')]
    return the_number_list
    

def get_value(instruction_values, instruction_number):
    return instruction_values[instruction_number]

def get_register(instruction_values, instruction_number, register_values):
    register_number = get_value(instruction_values, instruction_number)
    return register_values[register_number]

def set_register(instruction_values, instruction_number, register_values, value_to_set):
    register_number = get_value(instruction_values, instruction_number)
    register_values[register_number] = value_to_set

def add(left_value, right_value):
    return left_value + right_value

def mul(left_value, right_value):
    return left_value * right_value

def ban(left_value, right_value):
    return left_value & right_value

def bor(left_value, right_value):
    return left_value | right_value

def binary(register_values, instruction_values, opcode_name):
    # Implement logic to strip off the last letter and call function with the remaining letters
    # and use that last letter to determine which parameters will be sent
    left_value = get_register(instruction_values, 1, register_values)
    if opcode_name[-1] == 'r':
        right_value = get_register(instruction_values, 2, register_values)
    else:
        right_value = get_value(instruction_values, 2)
    function_to_call = opcode_name[:-1]
    result = eval(f'{function_to_call}(left_value,right_value)')
    set_register(instruction_values, 3, register_values, result)
    return register_values

def get_opcode_succ_list(register_values_initial, instruction_values, register_values_expected_final):
    opcode_succ_list = list()
    for opcode_name, operator_type in ALL_OPCODES.items():
        register_values = copy.deepcopy(register_values_initial)
        register_values = eval(f'{operator_type}( {register_values}, {instruction_values}, opcode_name )')
        if register_values_expected_final == register_values:
            opcode_succ_list.append(opcode_name)
    return opcode_succ_list


def get_count_opcodes_with_result(input_filename):
    register_values = None
    instruction_values = None
    opcode_succ_count = 0

    print(f'\nUsing input file: {input_filename}\n')
    # Reading input from the input file
    with open(input_filename) as f:
        # Pull in each line from the input file
        for line_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            if TEST:
                print(in_string)
            match line_number % 4:
                case 0:
                    if in_string[:7] != 'Before:':
                        break
                    register_values = get_number_list(in_string)
                case 1:
                    instruction_values = get_number_list(in_string)
                case 2:
                    matching_opcodes = get_opcode_succ_list(register_values, instruction_values, get_number_list(in_string))
                    opcode_succ_count += len(matching_opcodes)
                    if TEST:
                        print(f'The count of opcodes that match is: {opcode_succ_count}  ;  ', end = '')
                        print(f'Matching opcodes: {matching_opcodes}')

        # Sample test program ... not used in part 1

    print()
    
def solve_problem(input_filename):
    in_string = get_count_opcodes_with_result(input_filename)



solve_problem('input_sample0.txt')

# Function get_value returns element 1 from the list
def test_get_value():
    assert get_value([0,3,7,11], 1) == 3

# Function get_register first determines element 1 from the first list, which is 3
# and then it finds element 3 from the second list, which is 42
def test_get_register():
    assert get_register([0,3,7,11], 1, [39, 40, 41, 42, 43]) == 42

