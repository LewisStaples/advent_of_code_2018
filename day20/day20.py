def get_input_line(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f'The original input is: {in_string}')
    return in_string[1:-1]


def get_map(in_string):
    ret_val = dict()
    curr_locn = [0,0]
    ret_val[tuple(curr_locn)] = 'X'
    for ch in in_string:
        if ch == '(':
            # Temporarily disregarding branching
            # (I will come back to this later)
            break

        # Add new door to dict ret_val
        # Add new room to dict ret_val
        # Test both above to see if they're already there, and then test for any contradiction


    return ret_val


def solve_problem(input_filename):
    in_string = get_input_line(input_filename)
    get_map(in_string)
    print(f'Without start and end characters: {in_string}')
    print()

solve_problem('input_sample0.txt')
