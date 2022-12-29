from pathlib import Path

# read in the data file for day 3
with open("day5_input.txt", 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]


print(lines)