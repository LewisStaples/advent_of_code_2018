#!/usr/bin/env python3

# adventOfCode 2018 day 12
# https://adventofcode.com/2018/day/12


import copy

def get_input(input_filename):
    pattern__result = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
        print(in_string)
        initial_state = {i for i, ch in enumerate(in_string[15:]) if ch == '#'}
        print(initial_state)
        f.readline().rstrip()
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            if in_string[6:] == '=> #':
                pattern__result.append(in_string[:5])
    print()
    return initial_state, pattern__result


def run_iterations(initial_state, pattern__result, num_iterations):
    current_state = copy.deepcopy(initial_state)
    # new_state = set()
    # Loop through each iteration
    for _ in range(num_iterations):
        new_state = set()
        # Loop through each current plant, including two on each edge
        for i in range(min(current_state) - 2, max(current_state) + 3):
            # Construct string of the five pots or non-pots
            this_str = ''
            # Loop through the slice of five:  this plus two on each side
            for j in range(i-2, i+3):
                if j in current_state:
                    this_str += '#'
                else:
                    this_str += '.'
            if this_str in pattern__result:
                new_state.add(i)
        current_state = new_state
    return current_state


def second_function(list_of_sums, current_state):
    
    list_of_sums.append(sum(current_state))
    if len(list_of_sums) < 5:
        return 0
    
    target_diff =  list_of_sums[-1] - list_of_sums[-2]
    for i in range(1, 4):
        if target_diff != list_of_sums[-1 - i] - list_of_sums[-2 - i]:
            # actually, return from function
            # break
            return 0
    return target_diff

def some_function(initial_state, pattern__result):
    '''
    Detect when the pattern has stabilized to a gliding pattern
    '''
    current_state = copy.deepcopy(initial_state)
    # count_generations_passed = 0
    list_of_sums = []
    new_state = set()

    while True:

        new_state = set()
        # Loop through each current plant, including two on each edge
        for i in range(min(current_state) - 2, max(current_state) + 3):
            # Construct string of the five pots or non-pots
            this_str = ''
            # Loop through the slice of five:  this plus two on each side
            for j in range(i-2, i+3):
                if j in current_state:
                    this_str += '#'
                else:
                    this_str += '.'
            if this_str in pattern__result:
                new_state.add(i)
        current_state = new_state




        # count_generations_passed += 1
        sf_return = second_function(list_of_sums, current_state)
        if sf_return > 0:
            break


    
    dummy = 123
    # Return the answer to part 2 / part B
    return list_of_sums[-1] + (50000000000 - len(list_of_sums) ) * sf_return





def solve_problem(input_filename):
    initial_state, pattern__result = get_input(input_filename)

    # Solve problem 1/A:
    final_state_part1_A = run_iterations(initial_state, pattern__result, 20)
    print(f'The answer to part 1/A is: {sum(final_state_part1_A)}')

    # Solve problem 2/B:
    print(f'The answer to part 2/B is: {some_function(initial_state, pattern__result)}')


solve_problem('input.txt')




