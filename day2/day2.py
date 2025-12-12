import csv


def is_invalid(id: int) -> bool:
    """
    An invalid id is made only of some sequence of digits repeated twice

    55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs
    """
    id = str(id)

    # Odd ids cannot be invalid
    if len(id) % 2 == 1:
        return False

    # Check if the 2 parts are the same
    p1, p2 = id[:len(id)//2 + len(id)%2], id[len(id)//2 + len(id)%2:]
    return p1 == p2


def invalid_ids_in_range(start: int, stop: int) -> list[int]:
    invalid_ids = []
    for id in range(start, stop+1):
        if is_invalid(id):
            invalid_ids.append(id)
    return invalid_ids

INPUT_FILE = 'full.csv'
invalid_ids = []

with open(INPUT_FILE, newline='') as csvfile:
    id_ranges = csv.reader(csvfile)
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
print(f'Answer: {ans}')

