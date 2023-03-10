from pathlib import Path

# read in the data file for day 3
with open("day3_input.txt", 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]

#split the ruckscaks in half

rucksack_sum = 0
total_items = 0
for item in rucksacks:
    first_half = set(item[:len(item)//2])
    second_half = set(item[len(item)//2:])
    overlap = (first_half.intersection(second_half)).pop()
    print(total_items)
    total_items = total_items + 1

# translate to ascii and substract the base ('A' is 65, 'B' is 66 and so on) and add the new base
    if overlap.isupper():
        rucksack_sum += ord(overlap) - ord('A') + 27
        print(overlap, rucksack_sum)
    else:
        rucksack_sum += ord(overlap) - ord('a') + 1
        print(overlap, rucksack_sum)

print(rucksack_sum)

#part 2
rucksack_sum = 0
while len(rucksacks) > 0:
    first_rucksack = set(rucksacks.pop())
    second_rucksack = set(rucksacks.pop())
    third_rucksack = set(rucksacks.pop())
    overlap_new = ((first_rucksack.intersection(second_rucksack)).intersection(third_rucksack)).pop()

    if overlap_new.isupper():
        rucksack_sum += ord(overlap_new) - ord('A') + 27
    else:
        rucksack_sum += ord(overlap_new) - ord('a') + 1

print(rucksack_sum)

