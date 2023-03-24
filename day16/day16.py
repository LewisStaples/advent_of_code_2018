#!/usr/bin/env python3

# adventOfCode 2018 day 16
# https://adventofcode.com/2018/day/16

TEST = False
TEST = True


import copy
import numpy as np

# Storing the name of each operation, followed by the type of operator:  binary_, set_, or boolean_
#   binary_ calls a binary operator
#   set_ handles setting registers
#   boolean_ returns a boolean value, depending on whether a particular condition is met

ALL_OPCODES = {'addr': 'binary_', 'addi': 'binary_', 'mulr': 'binary_', 'muli':'binary_', 
               'banr':'binary_', 'bani':'binary_', 'borr':'binary_', 'bori':'binary_',
               'set_i':'set_', 'set_r':'set_',
               'gtir': 'boolean_', 'gtri': 'boolean_', 'gtrr': 'boolean_',
               'eqir': 'boolean_', 'eqri': 'boolean_', 'eqrr': 'boolean_',
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

def binary_(register_values, instruction_values, opcode_name):
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


def set_(register_values, instruction_values, opcode_name):
    # Implement logic to strip off the last letter and call function with the remaining letters
    # and use that last letter to determine whether "set register" or "set immediate"
    if opcode_name[-1] == 'r':
        value_to_copy = get_register(instruction_values, 1, register_values)
    else:
        value_to_copy = get_value(instruction_values, 1)
    set_register(instruction_values, 3, register_values, value_to_copy)
    return register_values

def gt(left_value, right_value):
    return left_value > right_value

def eq(left_value, right_value):
    return left_value == right_value

def boolean_(register_values, instruction_values, opcode_name):
    # Implement logic to strip off the last letter and call function with the remaining letters
    # and use that last letter to determine which parameters will be sent
    if opcode_name[-2] == 'r':
        left_value = get_register(instruction_values, 1, register_values)
    else:
        left_value = get_value(instruction_values, 1)
    if opcode_name[-1] == 'r':
        right_value = get_register(instruction_values, 2, register_values)
    else:
        right_value = get_value(instruction_values, 2)
    function_to_call = opcode_name[:-2]
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
    # working_map = dict()

    coeff_matrix = [None]*len(ALL_OPCODES)
    # np_opcodes = np.array(ALL_OPCODES.keys())

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

                    if TEST:
                        print(f'Matching opcodes: {matching_opcodes}')
                    if len(matching_opcodes) > 2:
                        opcode_succ_count += 1
                        if TEST:
                            print('This has at least three matching opcodes')
                    # working_map[instruction_values[0]] = matching_opcodes
                    coeff_matrix[instruction_values[0]] = [1 if opcode in matching_opcodes else 0 for opcode in ALL_OPCODES ]
                    # opcode_vector[instruction_values[0]] = len(matching_opcodes)

                    dummy = 123

        # Solve 
        opcode_to_function = dict()
        all_opcodes_keys = list(ALL_OPCODES.keys())
        # last_opcode_index = None
        prior_opcode_indices = []
        # for _ in range(len(ALL_OPCODES)):
        while len(prior_opcode_indices) < len(ALL_OPCODES):
            for c_m_index in range(len(ALL_OPCODES)):
                # if last_opcode_index is not None:
                #     coeff_matrix[c_m_index][last_opcode_index] = 0
                for prior_opcode_index in prior_opcode_indices:
                    coeff_matrix[c_m_index][prior_opcode_index] = 0
                if 1 == sum(coeff_matrix[c_m_index]):
                    # try:
                    opcode_to_function[c_m_index] = all_opcodes_keys[coeff_matrix[c_m_index].index(1)]
                    # except KeyError:
                    #     dummy = 123

                    # last_opcode_index = c_m_index
                    prior_opcode_indices.append(c_m_index)
                    # coeff_matrix[c_m_index][c_m_index] = 0
                    dummy = 123

                    # break

                # [c_m_index] = matching_opcodes[coeff_matrix[c_m_index].index(True)]
                dummy = 123



        # np_coeff_matrix = np.array(coeff_matrix)
        # np_opcode_vector = np.array(opcode_vector)
        # solution = np.linalg.solve(np_coeff_matrix, np_opcode_vector)

        # dummy = 123

    print(f'Count of opcodes with at least 3 matches (Part 1 Answer):  {opcode_succ_count}\n')
    
def solve_problem(input_filename):
    get_count_opcodes_with_result(input_filename)



solve_problem('input.txt')

# Function get_value returns element 1 from the list
def test_get_value():
    assert get_value([0,3,7,11], 1) == 3

# Function get_register first determines element 1 from the first list, which is 3
# and then it finds element 3 from the second list, which is 42
def test_get_register():
    assert get_register([0,3,7,11], 1, [39, 40, 41, 42, 43]) == 42

