#!/usr/bin/env python3

# adventOfCode 2018 day 16
# https://adventofcode.com/2018/day/16

TEST = False
TEST = True
# Storing the name of each operation, followed by the type of operator:  binary, unary, or conditional
ALL_OPCODES = {'addr': 'binary', 'addi': 'binary'}

def get_number_list(in_string):
    in_string = in_string.replace(',', '')
    # Truncate all text to the left of the first digit
    while not in_string[0].isdigit():
        in_string = in_string[1:]
    # Truncate all text to the right of the last digit
    while not in_string[-1].isdigit():
        in_string = in_string[:-1]
    # print(in_string)opcode_succ_count
    the_number_list = [int(num) for num in in_string.split(' ')]
    return the_number_list
    

def get_value(register_values, register_number):
    return register_values[register_number]

def get_register(register_values, register_number):
    the_value = get_value(register_values, register_number)
    return register_values[the_value]


def binary(register_values_init, instruction_values, register_values_final, opcode_name):
    # Implement logic to strip off the last letter and call function with the remaining letters
    # and use that last letter to determine which parameters will be sent
    pass

def get_opcode_succ_list(register_values_init, instruction_values, register_values_final):
    opcode_succ_list = list()
    for opcode_name, operator_type in ALL_OPCODES.items():
        print(f'{opcode_name = } , {operator_type = }')
        eval(f'{operator_type}( {register_values_init}, {instruction_values}, {register_values_final}, opcode_name )')
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
                    opcode_succ_count = get_opcode_succ_list(register_values, instruction_values, get_number_list(in_string))
                    if TEST:
                        print(f'{opcode_succ_count = }')
                    # if get_final_register_values(register_values, instruction_values) == get_number_list(in_string):
                    #     opcode_succ_count += 1


        # Sample test program ... not used in part 1

    print()
    
def solve_problem(input_filename):
    in_string = get_count_opcodes_with_result(input_filename)



solve_problem('input_sample0.txt')

def test_get_value():
    assert get_value([0,3,7,11], 1) == 3

def test_get_register():
    assert get_register([0,3,7,11], 1) == 11

