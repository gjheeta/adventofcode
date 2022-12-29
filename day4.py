from pathlib import Path

# read in the data file for day 3
with open("day4_input.txt", 'r') as f:
    lines = f.readlines()
    assignments = [entry.strip() for entry in lines]

def is_range_a_in_range_b(range_a, range_b):
    start_a, end_a = map(int, range_a.split('-'))
    start_b, end_b = map(int, range_b.split('-'))
    return start_b <= start_a and end_a <= end_b

number_of_contains = 0
for r in assignments:
    first_range, second_range = r.split(',')
    if is_range_a_in_range_b(first_range, second_range) or is_range_a_in_range_b(second_range, first_range):
        number_of_contains += 1

print(number_of_contains)

