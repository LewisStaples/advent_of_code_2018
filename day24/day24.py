#!/usr/bin/env python3

# adventOfCode 2018 day 24
# https://adventofcode.com/2018/day/24

from dataclasses import dataclass
from collections import namedtuple
from queue import PriorityQueue


@dataclass
class Group:
    unit_count: int
    hit_points: int
    attack_damage: int
    attack_type: str
    initiative: int
    paren_characterstics: dict

    def get_effective_power(self):
        return self.unit_count * self.attack_damage
    

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
                paren_characterstics = dict()
                if in_string[0] == '(':
                    paren_str, in_string = in_string[1:].split(') ')
                    paren_str_list = paren_str.split('; ')
                    for paren_ele in paren_str_list:
                        str1, str2 = paren_ele.split(' to ')
                        paren_characterstics[str1] = str2.split(', ')
                in_string = in_string.replace('with an attack that does ', '')
                in_string_list = in_string.split(' ', )
                the_input[army_name].groups.append(
                    Group(
                        int(the_unit_count_str),
                        int(the_hit_point_str),
                        int(in_string_list[0]),
                        in_string_list[1],
                        int(in_string_list[5]),

                        paren_characterstics
                        # # DUMMY VARIABLES ... NEED TO COMPLETE LOGIC HERE ....
                        # # weaknesses
                        # {''},
                        # # immunities
                        # {''}
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


    GroupID = namedtuple('GroupID', 
        ['ArmyName', 
            'GroupNumber']
    )

    # GroupOrderType = namedtuple('GroupOrderType', 
    #                             ['ArmyName', 
    #                                 'GroupNumber',
    #                                 'EffectivePower',
    #                                 'Initiative'])


    while keep_fighting:
        # Phase 1:  target selection
        
        # "In decreasing order of effective power, groups choose their targets; 
        # "in a tie, the group with the higher initiative chooses first
        GroupOrderRecords = PriorityQueue()
        for armyname in status:
            for the_group in status[armyname].groups:
                GroupOrderRecords.put((
                    (0 - the_group.get_effective_power(), 0 - the_group.initiative),
                    the_group
                ))

        fight_order = dict()
        while not GroupOrderRecords.empty():
            the_offense_group = GroupOrderRecords.get()[1]

            # "The attacking group chooses to target the group in the enemy army to which it would deal the most damage (after accounting for weaknesses and immunities, but not accounting for whether the defending group has enough units to actually receive all of that damage).

            # "If an attacking group is considering two defending groups to which it would deal equal damage, it chooses to target the defending group with the largest effective power; if there is still a tie, it chooses the defending group with the highest initiative. If it cannot deal any defending groups damage, it does not choose a target. Defending groups can only be chosen as a target by one attacking group.

            # Therefore, to choose the_defense_group to accompany the_offense_group, you should consider all groups that aren't yet assigned as the_defense_group to any the_offense_group, and review how the_defense_group's weaknesses and immunities impact the attack from the_offense_group.  After revewing all not yet assigned the_defense_group--s, choose the one that results in the_offense_group doing the most damage
            the_defense_group = None

            # Choose target, and index by initiative
            # print(f'{next_item}\n')
            AttackPairingType = namedtuple(
                'AttackPairingType',
                ['Attacker', 'Defender']
            )

            fight_order[the_offense_group.initiative] = AttackPairingType(
                the_offense_group,
                the_defense_group
            )

    # GroupOrderType = namedtuple('GroupOrderType', 
    #                             ['ArmyName', 
    #                                 'GroupNumber',
    #                                 'EffectivePower',
    #                                 'Initiative'])


        # Groups attack in decreasing order of initiative, regardless of whether they are part of the infection or the immune system. 




        # Phase 2:  attacking
        # Dummy stopping condition: combat ends once one army has lost all of its units
        keep_fighting = False

    # Answer: how many units would the winning army have
    return None


solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')


