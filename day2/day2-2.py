import csv
import textwrap


def is_invalid(id: int) -> bool:
    """
    An invalid id is made only of some sequence of digits repeated *at least* twice
    """
    id = str(id)
    # breakpoint()
    if len(id) == 1:
        return False

    # An ID of length n can be split at most n times
    for len_of_each_part in range(1, (len(id) // 2) + 1):
        if not (len(id) / len_of_each_part).is_integer():
            continue
        parts = textwrap.wrap(id, width=len_of_each_part)
        all_parts_same = len(set(parts)) == 1
        if all_parts_same:
            return True

    return False

assert is_invalid(5) == False
assert is_invalid(11) == True
assert is_invalid(43431) == False

def invalid_ids_in_range(start: int, stop: int) -> list[int]:
    invalid_ids = []
    for id in range(start, stop+1):
        if is_invalid(id):
            invalid_ids.append(id)
    return invalid_ids


def sol(input_file: str) -> int:
    invalid_ids = []

    with open(input_file, newline='') as csvfile:
        id_ranges = csv.reader(csvfile)
        # breakpoint()
        for fake_id_range in id_ranges:
            for id_range in fake_id_range:
                start_id, stop_id = id_range.split('-')
                start_id = int(start_id)
                stop_id = int(stop_id)
                range_invalid_ids = invalid_ids_in_range(start_id, stop_id)
                for invalid_id in range_invalid_ids:
                    invalid_ids.append(invalid_id)

    ans = 0
    for invalid_id in invalid_ids:
        ans += invalid_id

    return ans

sample_ans = sol('sample.csv')
sample_actual_ans = 4174379265
assert sample_ans == sample_actual_ans, f"Expected { sample_actual_ans }, got {sample_ans}"

small_ans = sol('small.csv')
small_actual_ans = 33
assert small_ans == small_actual_ans, f"Expected { small_actual_ans }, got {small_ans}"

print(f"Answer: {sol('full.csv')}")
