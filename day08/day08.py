#!/usr/bin/env python3

# adventOfCode 2018 day 8
# https://adventofcode.com/2018/day/8


def get_input(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    the_input = in_string.split(' ')
    the_input = [int(x) for x in the_input]
    return the_input


def analyze_node(node_list, node_ID = None):
    if node_ID is not None:
        print(f'Node {node_ID}: {node_list}')
        print(f'Header (first two elements): {node_list[:2]}')

        print(f'Metadata (last {node_list[1]} elements): {node_list[(node_list[1] * -1):]}')

def solve_problem(input_filename):
    all_nodes = get_input(input_filename)
    if len(all_nodes) < 20:
        analyze_node(all_nodes, 'A')
    else:
        analyze_node(all_nodes)


solve_problem('input_sample0.txt')

