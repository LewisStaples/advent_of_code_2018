def get_input_line(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f'The input is: {in_string}')
    return in_string[1:-1]


def solve_problem(input_filename):
    in_string = get_input_line(input_filename)
    print(f'Without start and end characters: {in_string}')
    print()

solve_problem('input_sample0.txt')
