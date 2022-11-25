# adventOfCode 2018 day 1
# https://adventofcode.com/2018/day/1


import sys


# Reading input from the input file into list
freq_change_list = []
input_filename='input_scenario0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        freq_change_list.append(int(in_string.rstrip().replace('+','')))


prev_seen_freqs = set()
freq_value = 0
while True:
    for freq_change in freq_change_list:
        freq_value += freq_change
        if freq_value in prev_seen_freqs:
            print(f'The final frequency (answer to Part B) is: {freq_value}\n')
            sys.exit('Program execution complete.\n')
        prev_seen_freqs.add(freq_value)

