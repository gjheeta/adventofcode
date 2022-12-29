from pathlib import Path
from typing import List

# read in the data file for day 5

with open("day5_input.txt", 'r') as f:
    lines = f.readlines()
    lines = [entry for entry in lines]

crate_lines = lines[:lines.index('\n')-1]
move_lines = lines[lines.index('\n')+1:]

