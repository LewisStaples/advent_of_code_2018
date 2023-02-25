#!/usr/bin/env python3

# adventOfCode 2018 day 14
# https://adventofcode.com/2018/day/14

DEBUG = False
scoreboard_and_elves = [[3, 7], 0, 1]


def get_input_number(input_filename):
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f'The input is: {in_string}', end = '')
    print()
    return int(in_string)


def display(scoreboard_and_elves):
    for the_index, val in enumerate(scoreboard_and_elves[0]):
        if the_index == scoreboard_and_elves[1]:
            print(f'({val})', end = '')
        elif the_index == scoreboard_and_elves[2]:
            print(f'[{val}]', end = '')
        else:
            print(f' {val} ', end = '')
    print()

def modify_scoreboard(input_number):
    while len(scoreboard_and_elves[0]) < (10 + input_number):

        # scoreboard_and_elves[0].append(0)
        calc_sum = scoreboard_and_elves[0][scoreboard_and_elves[1]]  + scoreboard_and_elves[0][scoreboard_and_elves[2]]
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
    dummy = 123


def get_last_ten_scores(input_number):
    ret_val = ''
    for i in range(input_number, input_number + 10):
        ret_val += str(scoreboard_and_elves[0][i])
    return ret_val


def solve_problem(input_filename):
    input_number = get_input_number(input_filename)
    modify_scoreboard(input_number)
    print(f'\nThe solution to part A is: {get_last_ten_scores(input_number)}\n')


solve_problem('input.txt')
