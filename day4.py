from pathlib import Path

# read in the data file for day 3
with open("day4_input.txt", 'r') as f:
    lines = f.readlines()
    assignments = [entry.strip() for entry in lines]

print(assignments)

