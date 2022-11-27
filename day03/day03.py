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

def get_claim_points(claim):
    ret_val = set()
    for x in range(claim.left_margin, claim.left_margin + claim.width):
        for y in range(claim.top_margin, claim.top_margin + claim.height):
            ret_val.add((x,y))
    return ret_val


    dummy = 123

def get_cpc_from_claims(claims):
    claim_point_count = dict()
    for claim_id, claim in claims.items():
        for claim_point in get_claim_points(claim):
            if claim_point in claim_point_count:
                claim_point_count[claim_point] += 1
            else:
                claim_point_count[claim_point] = 1

    return claim_point_count

def solve_problem(input_filename):
    # claim_point_count = dict()
    claims = get_claims_from_input(input_filename)
    claim_point_count = get_cpc_from_claims(claims)

    dummy = 123

    # for claim_id, claim in claims.items():
    #     if claim in claim_point_count:
    #         claim_point_count[claim] += 1
    #     else:
    #         claim_point_count[claim] = 1

# solve_problem('input.txt')
solve_problem('input_sample0.txt')

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

def test_single_line_get_points():
    claims = get_claims_from_input('input_sample0.txt')
    assert len(claims) == 1
    assert '123' in claims
    assert (2,2) not in get_claim_points(claims['123'])
    assert (3,1) not in get_claim_points(claims['123'])
    assert (3,2) in get_claim_points(claims['123'])
    assert (7,2) in get_claim_points(claims['123'])
    assert (7,1) not in get_claim_points(claims['123'])
    assert (8,2) not in get_claim_points(claims['123'])
    assert (2,5) not in get_claim_points(claims['123'])
    assert (3,5) in get_claim_points(claims['123'])
    assert (7,5) in get_claim_points(claims['123'])
    assert (8,5) not in get_claim_points(claims['123'])

