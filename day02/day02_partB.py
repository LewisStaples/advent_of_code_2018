# adventOfCode 20xy day 2
# https://adventofcode.com/20xy/day/2


from itertools import combinations
from scipy.spatial.distance import hamming 
import sys


boxID_list = []
# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        boxID_list.append(list(in_string))

for id1, id2 in combinations(boxID_list, 2):
    if int(hamming(id1, id2) * len(id1)) == 1:
        common_ltrs = [ch for i, ch in enumerate(id1) if id1[i] == id2[i]]
        common_ltrs = ''.join(common_ltrs)
        print(f"The letters common to both ID's that differ by one char. (the answer to B) is: {common_ltrs}\n")
        sys.exit('Program exiting successfully\n')

