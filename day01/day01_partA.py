# adventOfCode 2018 day 1
# https://adventofcode.com/2018/day/1

freq_value = 0

# Reading input from the input file
input_filename='input_scenario0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        freq_change = int(in_string.rstrip().replace('+',''))
        freq_value += freq_change

print(f'The final frequency (answer to Part A) is: {freq_value}\n')


