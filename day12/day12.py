#!/usr/bin/env python3

# adventOfCode 2018 day 12
# https://adventofcode.com/2018/day/12


import copy


def get_input(input_filename):
    """
    This function reads the input file,
    and it returns two data structures from reading the input
    """
    pattern_result = list()
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
        initial_state = {i for i, ch in enumerate(in_string[15:]) if ch == "#"}
        f.readline().rstrip()
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            if in_string[6:] == "=> #":
                pattern_result.append(in_string[:5])
    return initial_state, pattern_result


def run_iterations(initial_state, pattern_result, num_iterations):
    """
    This function is used to run a fixed number of iterations.
    The final state is returned.
    (This is used to solve problem 1/A)
    """
    current_state = copy.deepcopy(initial_state)
    # Loop through each iteration
    for _ in range(num_iterations):
        current_state = get_state_after_iteration(current_state, pattern_result)
    return current_state


def get_difference_when_gliding(list_of_sums, current_state):
    """
    This function returns 0 if the input indicates that not enough
    iterations have been performed to reach where it glides.
    Once gliding is detected, it returns the difference bewteen adjacent iterations.
    """
    list_of_sums.append(sum(current_state))
    if len(list_of_sums) < 5:
        # Not completed yet
        return 0
    target_diff = list_of_sums[-1] - list_of_sums[-2]
    for i in range(1, 4):
        if target_diff != list_of_sums[-1 - i] - list_of_sums[-2 - i]:
            # Not completed yet
            return 0
    # It is completed now
    return target_diff


def get_state_after_iteration(current_state, pattern_result):
    """
    This function performs an iteration, and it returns the subsequent state
    """
    new_state = set()
    # Loop through each current plant, including two on each edge
    for i in range(min(current_state) - 2, max(current_state) + 3):
        # Construct string of the five pots or non-pots
        this_str = ""
        # Loop through the slice of five:  this plus two on each side
        for j in range(i - 2, i + 3):
            if j in current_state:
                this_str += "#"
            else:
                this_str += "."
        if this_str in pattern_result:
            new_state.add(i)
    return new_state


def get_number_sum_after_50bil_iterations(initial_state, pattern_result):
    """
    Detect when the pattern has stabilized to a gliding pattern
    """
    current_state = copy.deepcopy(initial_state)
    list_of_sums = []
    while True:
        current_state = get_state_after_iteration(current_state, pattern_result)
        sf_return = get_difference_when_gliding(list_of_sums, current_state)
        if sf_return > 0:
            break
    # Return the answer to part 2 / part B
    return list_of_sums[-1] + (50000000000 - len(list_of_sums)) * sf_return


def solve_problem(input_filename):
    initial_state, pattern_result = get_input(input_filename)
    # Solve problem 1/A:
    final_state_part1_A = run_iterations(initial_state, pattern_result, 20)
    print(f"The answer to part 1/A is: {sum(final_state_part1_A)}")
    # Solve problem 2/B:
    print(
        f"The answer to part 2/B is: \
{get_number_sum_after_50bil_iterations(initial_state, pattern_result)}"
    )
    print()


solve_problem("input.txt")
