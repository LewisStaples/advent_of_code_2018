#!/usr/bin/env python3

# adventOfCode 2018 day 8
# https://adventofcode.com/2018/day/8


def get_input(input_filename):
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    the_input = in_string.split(" ")
    the_input = [int(x) for x in the_input]
    return the_input


def analyze_node(node_list, node_ID, start_index):
    # Display information
    if len(node_list) < 20:
        print(
            f"Node {node_ID}'s Header (first two elements)\
: {node_list[start_index : start_index + 2]}"
        )
    child_index = start_index + 2
    metadata_sum = 0
    node_value = 0
    node_values = list()
    for i in range(node_list[start_index]):
        return_values = analyze_node(node_list, f"{node_ID}-{i+1}", child_index)
        child_index = return_values[0]
        metadata_sum += return_values[1]
        node_values.append(return_values[2])

    for _ in range(node_list[start_index + 1]):
        metadata_sum += node_list[child_index]
        if node_list[child_index] - 1 < len(node_list):
            if len(node_values) > node_list[child_index] - 1:
                node_value += node_values[node_list[child_index] - 1]
        child_index += 1

    if len(node_values) == 0:
        node_value = metadata_sum

    return child_index, metadata_sum, node_value


def solve_problem(input_filename):
    all_nodes = get_input(input_filename)
    if len(all_nodes) < 20:
        print(f"Node Root: {all_nodes}")
    return_values = analyze_node(all_nodes, "Root", 0)
    print(f"The sum of metadata is {return_values[1]}")
    print(f"The value of the root node is {return_values[2]}")


solve_problem("input_sample0.txt")
