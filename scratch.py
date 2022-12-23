import re

myList = [1000,2000,3000,'',4000,'',5000,6000,'',7000,8000,9000,'',10000]
result = [[]]
for i in myList:
    if not i:
        result.append([])
    else:
        result[-1].append(i)
print(result)


