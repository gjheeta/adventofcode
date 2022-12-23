from pathlib import Path
import re

#read in the data file
data = Path("day1_input.txt").read_text().split("\n")

#split the data from the file in a list of lists
result = [[]]
for i in data:
    if not i:
        result.append([])
    else:
        result[-1].append(int(i))
print(result)

#sum each list of list
sumvalues = []
for i in result:
    sumvalues.append(sum(i))

#get the maximum index
max_index = sumvalues.index(max(sumvalues))
print(max_index)

print(result[max_index])
print(sumvalues[max_index])

# Get the top three values and sum these
sumvalues.sort(reverse=True)
first = sumvalues[0]
second = sumvalues[1]
third = sumvalues[2]
print(sum([first, second, third]))
