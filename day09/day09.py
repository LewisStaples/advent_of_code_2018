#!/usr/bin/env python3

# adventOfCode 2018 day 09
# https://adventofcode.com/20xy/day/9


from dataclasses import dataclass


def get_input_values(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    ret_val = list()
    with open(input_filename) as f:
        while True:
            in_string = f.readline().rstrip()
            if len(in_string) == 0:
                break
            player_count, str2 = in_string.split(' players; last marble is worth ')
            last_marble_value, str3 = str2.split(' points')
            ret_val.append(tuple((int(player_count), int(last_marble_value))))
    return ret_val

@dataclass
class Circle:
    current_index: int
    marble_circle: list

    def update(self, next_marble):
        '''
        The update method handles updates to the circle of marbles in a particular turn.
        The return value is the amount to be added to the player's score.
        '''

        # Update circle by removing a marble (don't insert next_marble)
        if next_marble % 23 == 0:
            ret_val = next_marble
            self.current_index -= 7
            self.current_index %= len(self.marble_circle)
            # print(f'Removing marble {self.marble_circle[self.current_index]} from index {self.current_index} ...')
            ret_val += self.marble_circle.pop(self.current_index)
            return ret_val
        
        # Update by inserting a new marble
        self.current_index = (self.current_index + 2) % len(self.marble_circle)
        self.marble_circle.insert(self.current_index, next_marble)
        return 0

    def __repr__(self):
        ret_val = '['
        i_zero = self.marble_circle.index(0)
        for i in (list(range(i_zero, len(self.marble_circle))) + list(range(i_zero))):
            val = self.marble_circle[i]
            this_portion = f'{val}'
            if i == self.current_index:
                this_portion = '(' + this_portion + ')'

            this_portion += ', '

            ret_val += this_portion

        ret_val += ']'
        return ret_val

def solve_problem(i_v):
    player_count, last_marble_value = i_v
    print(f'Using player count {player_count}, and last marble value {last_marble_value}: ', end='')
    circle = Circle(0, [0])
    player_scores = {x:0 for x in range(1, player_count + 1)}
    for next_marble in range(1, last_marble_value + 1):
        player_number = (next_marble - 1) % player_count + 1
        player_scores[player_number] += circle.update(next_marble)
        # print(f'Player {player_number}, circle: ', end='')
        # print(circle)
    # print()
    print(f'high score is {max(player_scores.values())}')

def open_input_file(input_filename):
    input_values = get_input_values(input_filename)
    for i_v in input_values:
        solve_problem(i_v)
    print()


open_input_file('input.txt')


