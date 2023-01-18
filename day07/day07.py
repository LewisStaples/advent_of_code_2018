#!/usr/bin/env python3

# adventOfCode 2018 day 7
# https://adventofcode.com/2018/day/7


import copy


def get_input(input_filename):
    """
    Read input, and return a tuple with two elements:
    
    The first tuple element is a Python dict that represents the given rules.
    Each key is a step that cannot be started without at least one other step completed.
    When complete, each value is a comprehensive list of all steps that must be
    completed before the step in the key can be started.

    The second tuple element is a set that lists all steps that appear as a 
    prerequisite to another step in the rules.
    """
    rules = dict()
    steps_before_other_steps = set()

    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
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
    rules_local = copy.deepcopy(rules)
    while len(available_steps) > 0:
        available_steps.sort()
        this_step = available_steps.pop(0)
        step_order.append(this_step)
        for later_step, earlier_steps in rules_local.items():
            if this_step in earlier_steps:
                rules_local[later_step].remove(this_step)
                if len(rules_local[later_step]) == 0:
                    available_steps.append(later_step)
    step_order = "".join(step_order)
    return step_order


def get_completion_time(rules, steps_before_other_steps):
    completed_steps = list()
    workers = dict()
    if len(rules) == 5:
        worker_count = 2
        step_time_adder = 0
    else:
        worker_count = 5
        step_time_adder = 60
    available_steps = list(steps_before_other_steps - rules.keys())
    available_steps.sort()

    stopwatch = 0
    while True:
        # Assign an available step to a worker (if possible)
        while len(workers) < worker_count and len(available_steps) > 0:
            this_step = available_steps.pop(0)
            workers[this_step] = step_time_adder + ord(this_step) - ord("A") + 1

        # Count down workers' timer to work on their assigned issues
        worker_ids = list(workers.keys())
        for step_id in worker_ids:
            if workers[step_id] > 1:
                workers[step_id] -= 1
            else:
                workers.pop(step_id)
                completed_steps.append(step_id)

                # See if any new steps have been available, now that step_id is finished
                for later_step, earlier_steps in rules.items():
                    if step_id in earlier_steps:
                        rules[later_step].remove(step_id)
                        if len(rules[later_step]) == 0:
                            available_steps.append(later_step)

        stopwatch += 1

        if len(available_steps) + len(workers) == 0:
            return stopwatch


def solve_problem(input_filename):
    rules, steps_before_other_steps = get_input(input_filename)
    step_order = get_step_order(rules, steps_before_other_steps)
    print(f"The solution to part A is: {step_order}\n")
    completion_time = get_completion_time(rules, steps_before_other_steps)
    print(f"The solution to part B is: {completion_time}\n")


solve_problem("input.txt")
