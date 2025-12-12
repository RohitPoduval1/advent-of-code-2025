"""
One could use a nested for loop to get the answer, but this is O(n^2).
Santa needs to visit the ENTIRE WORLD in ONE NIGHT.
Quadratic vs linear time matters in scenarios like these...
"""
import time


def get_max_joltage_n_squared(bank: str) -> int:
    max_joltage = -1
    for tens_i in range(len(bank)-1):
        for ones_i in range(tens_i + 1, len(bank)):
            joltage = 10*int(bank[tens_i]) + int(bank[ones_i])
            max_joltage = max(joltage, max_joltage)

    return max_joltage


def get_max_joltage(bank: str) -> int:
    # Make one pass to get the largest 10s digit
    largest_tens_i = 0
    for i, num in enumerate(bank[:-1]):
        if int(bank[i]) > int(bank[largest_tens_i]):
            largest_tens_i = i

    # Make another pass to get the largest 1s digit
    largest_ones_i = largest_tens_i + 1
    for i in range(largest_tens_i + 1, len(bank)):
        num = int(bank[i])
        if num > int(bank[largest_ones_i]):
            largest_ones_i = i

    max_joltage = 10*int(bank[largest_tens_i]) + int(bank[largest_ones_i])
    return max_joltage


INPUT_FILE = 'final.txt'
total_joltage = 0
with open(INPUT_FILE) as f:
    start_time = time.time()
    for bank in f:
        bank = bank.strip()
        max_bank_joltage = get_max_joltage(bank)
        total_joltage += max_bank_joltage
    end_time = time.time()

print(f'O(n) Answer: {total_joltage} in {end_time - start_time} seconds')

total_joltage = 0
with open(INPUT_FILE) as f:
    start_time = time.time()
    for bank in f:
        bank = bank.strip()
        max_bank_joltage = get_max_joltage_n_squared(bank)
        total_joltage += max_bank_joltage
    end_time = time.time()

print(f'O(n^2) Answer: {total_joltage} in {end_time - start_time} seconds')
