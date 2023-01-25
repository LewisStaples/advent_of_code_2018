#!/usr/bin/env python3

# adventOfCode 2018 day 09
# https://adventofcode.com/20xy/day/9


def get_input_values(input_filename):
    print(f"\nUsing input file: {input_filename}\n")
    ret_val = list()
    with open(input_filename) as f:
        while True:
            in_string = f.readline().rstrip()
            if len(in_string) == 0:
                break
            player_count, str2 = in_string.split(" players; last marble is worth ")
            last_marble_value, str3 = str2.split(" points")
            ret_val.append(tuple((int(player_count), int(last_marble_value))))
    return ret_val


class MarbleNode:
    def __init__(self, number):
        self.number = number
        self.next = None
        self.prev = None

    def label_next(self, next):
        self.next = next

    def label_prev(self, prev):
        self.prev = prev

    def __repr__(self):
        return str(self.number)


class Circle:
    def __init__(self):
        self.marble_node = MarbleNode(0)
        self.current_node = self.marble_node
        self.ORIGINAL_NODE = self.marble_node  # for printing

        self.marble_node.next = self.marble_node
        self.marble_node.prev = self.marble_node

    def update(self, latest_marble_value):
        """
        The update method handles updates to the circle of marbles in a particular turn.
        The return value is the amount to be added to the player's score.
        """

        # Update circle by removing a marble (don't insert next_marble)
        if latest_marble_value % 23 == 0:
            ret_val = latest_marble_value

            # Adjust current node CCW by 7 marbles
            for _ in range(7):
                self.current_node = self.current_node.prev

            # Include current node in player's score and remove it from the circle
            ret_val += self.current_node.number
            prior_node = self.current_node.prev
            next_node = self.current_node.next
            prior_node.label_next(next_node)
            next_node.label_prev(prior_node)
            self.current_node = next_node
            return ret_val

        latest_marble_node = MarbleNode(latest_marble_value)
        self.current_node = self.current_node.next
        current_next = self.current_node.next

        latest_marble_node.label_next(current_next)
        latest_marble_node.label_prev(self.current_node)
        self.current_node.label_next(latest_marble_node)
        current_next.label_prev(latest_marble_node)

        self.current_node = latest_marble_node
        return 0

    def __repr__(self):
        ret_val = "["
        this_node = self.ORIGINAL_NODE
        ret_val += str(this_node) + ", "
        while this_node.next != self.ORIGINAL_NODE:
            this_node = this_node.next
            if this_node == self.current_node:
                ret_val += "(" + str(this_node) + "), "
            else:
                ret_val += str(this_node) + ", "
        ret_val += "]"
        return ret_val


def solve_problem(i_v):
    player_count, last_marble_value = i_v
    print(
        f"With player count {player_count}, and last marble value {last_marble_value}: "
    )
    circle = Circle()
    player_scores = {x: 0 for x in range(1, player_count + 1)}
    for next_marble in range(1, last_marble_value + 1):
        player_number = (next_marble - 1) % player_count + 1
        player_scores[player_number] += circle.update(next_marble)

    print(f"Part 1 / Part A high score is {max(player_scores.values())}")

    circle = Circle()
    player_scores = {x: 0 for x in range(1, player_count + 1)}
    for next_marble in range(1, 100 * last_marble_value + 1):
        player_number = (next_marble - 1) % player_count + 1
        player_scores[player_number] += circle.update(next_marble)
    print(f"Part 1 / Part B high score is {max(player_scores.values())}")


def open_input_file(input_filename):
    input_values = get_input_values(input_filename)
    for i_v in input_values:
        solve_problem(i_v)
    print()


open_input_file("input_sample0.txt")
