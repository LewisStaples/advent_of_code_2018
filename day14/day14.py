#!/usr/bin/env python3

# adventOfCode 2018 day 14
# https://adventofcode.com/2018/day/14

scoreboard_and_elves = [[3, 7], 0, 1]


def get_input_number(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    # print(f'The input is: {in_string}')
    return int(in_string)


def modify_scoreboard(input_number):
    while len(scoreboard_and_elves[0]) < (10 + input_number):
        # scoreboard_and_elves[0].append(0)
        calc_sum = scoreboard_and_elves[0][scoreboard_and_elves[1]]  + scoreboard_and_elves[0][scoreboard_and_elves[2]]
        tens_digit = (calc_sum + 1) // 10
        ones_digit = calc_sum % 10
        if tens_digit > 0:
            scoreboard_and_elves[0].append(tens_digit)
        scoreboard_and_elves[0].append(ones_digit)
        scoreboard_and_elves[1] += tens_digit + 1
        scoreboard_and_elves[2] += ones_digit + 1
        scoreboard_and_elves[1] %= len(scoreboard_and_elves[0])
        scoreboard_and_elves[2] %= len(scoreboard_and_elves[0])
    dummy = 123



def solve_problem(input_filename):
    input_number = get_input_number(input_filename)
    modify_scoreboard(input_number)



solve_problem('input_sample0.txt')









