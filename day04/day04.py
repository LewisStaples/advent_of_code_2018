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

def get_guard_id_with_most_total_sleep(guard_records):
    # guard_totals is a temporary dict with guard_id and that guard's total time asleep
    guard_totals = dict()
    for guard in guard_records:
        guard_totals[guard] = sum(guard_records[guard].values())
    max_total = max(guard_totals.values())
    ret_val = [k for (k,v) in guard_totals.items() if v == max_total][0]
    return ret_val

def get_minute_most_sleep(guard_id, guard_records):
    max_count = max(guard_records[guard_id].values())
    ret_val = [k for (k,v) in guard_records[guard_id].items() if v == max_count][0]
    return ret_val

def solve_problem(input_filename):
    sorted_records = get_input_lines_sorted(input_filename)
    guard_records = get_guard_records(sorted_records)
    guard_id_with_most_total_sleep = get_guard_id_with_most_total_sleep(guard_records)
    minute_that_most_sleepy_guard_is_most_likely_asleep = get_minute_most_sleep(guard_id_with_most_total_sleep, guard_records)
    print(f'The answer to part A is {guard_id_with_most_total_sleep * minute_that_most_sleepy_guard_is_most_likely_asleep}\n')

solve_problem('input_sample0.txt')

    

