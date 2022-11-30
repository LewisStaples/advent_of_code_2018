import string

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
    polymer_latest = get_input_line(input_filename)
    while True:
        polymer_len = len(polymer_latest)
        for pair in all_pairs:
            polymer_latest = polymer_latest.replace(pair, '')
        if len(polymer_latest) == polymer_len:
            break
    print(f'The answer to part A is {len(polymer_latest)}\n')

solve_problem('input_sample0.txt')
