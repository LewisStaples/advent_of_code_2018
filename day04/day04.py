# adventOfCode 2018 day 4
# https://adventofcode.com/2018/day/4


def get_input_lines_sorted(input_filename):
    ret_val = []
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            ret_val.append(in_string)
    return sorted(ret_val)

def solve_problem(input_filename):
    sorted_records = get_input_lines_sorted(input_filename)

solve_problem('input_sample0.txt')

    

