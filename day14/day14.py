#!/usr/bin/env python3

# adventOfCode 2018 day 14
# https://adventofcode.com/2018/day/14

DEBUG = False
scoreboard_and_elves = [[3, 7], 0, 1]


def get_input_string(input_filename):
    print(f"\nUsing input file: {input_filename}")
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f"The input is: {in_string}", end="")
    print()
    return in_string


def display(scoreboard_and_elves):
    for the_index, val in enumerate(scoreboard_and_elves[0]):
        if the_index == scoreboard_and_elves[1]:
            print(f"({val})", end="")
        elif the_index == scoreboard_and_elves[2]:
            print(f"[{val}]", end="")
        else:
            print(f" {val} ", end="")
    print()


def expand_scoreboard(number_indices_to_add):
    for i in range(number_indices_to_add):
        calc_sum = (
            scoreboard_and_elves[0][scoreboard_and_elves[1]]
            + scoreboard_and_elves[0][scoreboard_and_elves[2]]
        )
        tens_digit = (calc_sum) // 10
        ones_digit = calc_sum % 10

        if tens_digit > 0:
            scoreboard_and_elves[0].append(tens_digit)
        scoreboard_and_elves[0].append(ones_digit)

        scoreboard_and_elves[1] += 1 + scoreboard_and_elves[0][scoreboard_and_elves[1]]
        scoreboard_and_elves[2] += 1 + scoreboard_and_elves[0][scoreboard_and_elves[2]]
        scoreboard_and_elves[1] %= len(scoreboard_and_elves[0])
        scoreboard_and_elves[2] %= len(scoreboard_and_elves[0])

        if DEBUG:
            display(scoreboard_and_elves)


def get_first_answer(smallest_index_to_report_str):
    ret_val = ""
    smallest_index_to_report_int = int(smallest_index_to_report_str)
    for i in range(smallest_index_to_report_int, smallest_index_to_report_int + 10):
        ret_val += str(scoreboard_and_elves[0][i])
    return ret_val


def get_second_answer(input_string):
    list_digits_to_match = list(map(lambda x: int(x), input_string))
    scoreboard_index = 0
    while True:
        # Evaluating if scoreboard values starting with
        # scoreboard_index match list_digits_to_match
        for match_index in range(len(list_digits_to_match)):
            if (
                scoreboard_and_elves[0][scoreboard_index + match_index]
                != list_digits_to_match[match_index]
            ):
                # Match not yet found, so break from for loop
                break

            if match_index == len(list_digits_to_match) - 1:
                # A match has been found
                return scoreboard_index
        scoreboard_index += 1
        # If there aren't enough slots on the scoreboard, then expand it
        if scoreboard_index + len(list_digits_to_match) >= len(scoreboard_and_elves[0]):
            expand_scoreboard(100)


def solve_problem(input_filename):
    input_string = get_input_string(input_filename)

    expand_scoreboard(int(input_string) + 10)
    print(f"\nThe solution to part 1/A is: {get_first_answer(input_string)}\n")

    print(f"\nThe solution to part 2/B is: {get_second_answer(input_string)}\n")


solve_problem("input_sample1.txt")
