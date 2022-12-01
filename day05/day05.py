import string
import copy


def get_input_line(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_polymer_latest = f.readline().rstrip()
    print(f'The input is {len(in_polymer_latest)} chars long, and it starts with:  {in_polymer_latest[:10]}\n')
    return in_polymer_latest

def get_all_pairs():
    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)
    all_pairs = [''.join(x) for x in zip(lower_list, upper_list)]
    reverse_pairs = [x[1] + x[0] for x in all_pairs]
    all_pairs = all_pairs + reverse_pairs
    return all_pairs

def solve_problem(input_filename):
    all_pairs = get_all_pairs()
    polymer_original = get_input_line(input_filename)
    polymer_latest = copy.deepcopy(polymer_original)

    # Solve part A
    while True:
        polymer_len = len(polymer_latest)
        for pair in all_pairs:
            polymer_latest = polymer_latest.replace(pair, '')
        if len(polymer_latest) == polymer_len:
            break
    print(f'The answer to part A is {len(polymer_latest)}\n')

    # Solve part B
    shortest_len = float('inf')
    for i in range(26):
        polymer_copy = copy.deepcopy(polymer_original)
        uppercase_char = chr(ord('A') + i)
        while True:
            polymer_len = len(polymer_copy)
            polymer_copy = polymer_copy.replace(uppercase_char, '')
            if len(polymer_copy) == polymer_len:
                break
        lowercase_char = chr(ord('a') + i)
        while True:
            polymer_len = len(polymer_copy)
            polymer_copy = polymer_copy.replace(lowercase_char, '')
            if len(polymer_copy) == polymer_len:
                break

        while True:
            polymer_len = len(polymer_copy)
            for pair in all_pairs:
                polymer_copy = polymer_copy.replace(pair, '')
            if len(polymer_copy) == polymer_len:
                shortest_len = min(shortest_len, len(polymer_copy))
                break
    print(f'The answer to part B is {shortest_len}\n')

solve_problem('input.txt')
