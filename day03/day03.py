# adventOfCode 2018 day 03
# https://adventofcode.com/2018/day/03


from collections import namedtuple


Claim = namedtuple('Claim', ['left_margin', 'top_margin', 'width', 'height'])


def get_claims_from_input(input_filename):
    claims_collection = dict()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            left_str, right_str = in_string.split(' @ ')
            claim_id = left_str.replace('#', '')
            left_margin, right_str = right_str.split(',')
            left_margin = int(left_margin)
            top_margin, right_str = right_str.split(': ')
            top_margin = int(top_margin)
            width, height = right_str.split('x')
            width = int(width)
            height = int(height)
            claims_collection[claim_id] = Claim(left_margin, top_margin, width, height)
    return claims_collection

def solve_problem(input_filename):
    claims = get_claims_from_input(input_filename)

solve_problem('input.txt')

def test_single_line_input():
    claims = get_claims_from_input('input_sample0.txt')
    assert len(claims) == 1
    assert claims['123'] == Claim(3, 2, 5, 4)

def test_multiple_line_input():
    claims = get_claims_from_input('input_sample1.txt')
    assert len(claims) == 3
    assert claims['1'] == Claim(1, 3, 4, 4)
    assert claims['2'] == Claim(3, 1, 4, 4)
    assert claims['3'] == Claim(5, 5, 2, 2)

