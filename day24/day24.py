#!/usr/bin/env python3

# adventOfCode 2018 day 24
# https://adventofcode.com/2018/day/24

from dataclasses import dataclass


@dataclass
class Group:
    unit_count: int
    hit_points: int
    attack_damage: int
    attack_type: str
    initiative: int
    weaknesses: set[str]
    immunities: set[str]

# @dataclass
class Army:
    army_name: str  # immune system, infection
    groups: list # list[Group]

    def __init__(self, army_name):
        self.army_name = army_name
        self.groups = list()
    
    def add_group(self, new_group):
        self.groups.append(new_group)
    

def get_input(input_filename):
    the_input = dict()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            if len(in_string) < 2:
                # If line is empty, ignore it
                continue
            if 'units' not in in_string:
                # If it's a new army, start compiling info about the new army
                army_name = in_string.replace(':','')
                the_input[army_name] = Army(army_name)
            else:
                # It must be a new group
                print(in_string)
                the_unit_count_str, in_string = in_string.split(' units each with ')
                the_hit_point_str, in_string = in_string.split(' hit points ')
                if in_string[0] == '(':
                    paren_str, in_string = in_string[1:].split(') ')
                    paren_str_list = paren_str.split('; ')
                    dummy = 123
                in_string = in_string.replace('with an attack that does ', '')
                in_string_list = in_string.split(' ', )
                the_input[army_name].groups.append(
                    Group(
                        int(the_unit_count_str),
                        int(the_hit_point_str),
                        int(in_string_list[0]),
                        in_string_list[1],
                        int(in_string_list[5]),

                        # DUMMY VARIABLES ... NEED TO COMPLETE LOGIC HERE ....
                        {''},
                        {''}
                    )
                )
                dummy = 123

                continue  # TO BE IMPLEMENTED LATER ....
            print(in_string)
    print()
    return the_input
    
def solve_problem(input_filename):
    status = get_input(input_filename)
    keep_fighting = True
    
    while keep_fighting:
        # Phase 1:  target selection
        # Phase 2:  attacking
        # Dummy stopping condition: combat ends once one army has lost all of its units
        keep_fighting = False

    # Answer: how many units would the winning army have
    return None


solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')

