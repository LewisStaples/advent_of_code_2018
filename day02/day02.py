# adventOfCode 20xy day 2
# https://adventofcode.com/20xy/day/2


from collections import Counter

total_freq_counts = dict()

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        the_counter = Counter(in_string)
        freq_counts = set(the_counter.values())
        for fc in freq_counts:
            if fc not in total_freq_counts:
                total_freq_counts[fc] = 1
            else:
                total_freq_counts[fc] += 1

print(f'The checksum (answer to A) is: {total_freq_counts[2] * total_freq_counts[3]}\n')


