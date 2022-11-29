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
            # in_string.replace(' 00:', ' 24:')
            ret_val.append(in_string)
    return sorted(ret_val)

def get_guard_records(sorted_records):
    ret_val = dict()
    current_guard = None
    timestamp_sleep_started = None
    for record in sorted_records:
        if 'begins shift' in record:
            current_guard = int(record[26:-13])
        elif 'falls asleep' in record:
            timestamp_sleep_started = record[1:17]
        elif 'wakes up' in record:
            assert record[1:11] == timestamp_sleep_started[:10] # Assert same date (this was a given)
            assert record[12:14] == timestamp_sleep_started[11:13] == '00' # Assert hours are 00 (given)
            sleep_end_minutes = int(record[15:17])
            sleep_start_minutes = int(timestamp_sleep_started[14:])

            if current_guard not in ret_val:
                ret_val[current_guard] = dict()
            for sleep_timestamp in range(sleep_start_minutes, sleep_end_minutes):
                if sleep_timestamp not in ret_val[current_guard]:
                    ret_val[current_guard][sleep_timestamp] = 1
                else:
                    ret_val[current_guard][sleep_timestamp] += 1
        else:
            raise ValueError(f'Strange input record:  {record}')

    return ret_val

def solve_problem(input_filename):
    sorted_records = get_input_lines_sorted(input_filename)
    guard_records = get_guard_records(sorted_records)
    dummy = 123

solve_problem('input_sample0.txt')

    

