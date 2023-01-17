#!/usr/bin/env python3

# adventOfCode 2018 day 7
# https://adventofcode.com/2018/day/7


def get_input(input_filename):
    '''
    Read input, and return a Python dict that represents the given rules.
    Each key is a step that cannot be started without at least one other step completed.
    When complete, each value is a comprehensive list of all steps that must be
    completed before the step in the key can be started.
    '''
    rules = dict()
    steps_before_other_steps = set()

    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()

            earlier_step = in_string[5]
            later_step = in_string[36]

            if later_step not in rules:
                rules[later_step] = []
            rules[later_step].append(earlier_step)
            steps_before_other_steps.add(earlier_step)

    return rules, steps_before_other_steps

def get_step_order(rules, steps_before_other_steps):
    step_order = []
    available_steps = list(steps_before_other_steps - rules.keys())
    while len(available_steps) > 0:
        available_steps.sort()
        this_step = available_steps.pop(0)
        step_order.append(this_step)
        for later_step, earlier_steps in rules.items():
            if this_step in earlier_steps:
                rules[later_step].remove(this_step)
                if len(rules[later_step]) == 0:
                    available_steps.append(later_step)
    step_order = ''.join(step_order)
    return step_order

def solve_problem(input_filename):
    rules, steps_before_other_steps = get_input(input_filename)
    step_order = get_step_order(rules, steps_before_other_steps)
    print(f'The solution to A is: {step_order}\n')
solve_problem('input_sample0.txt')

