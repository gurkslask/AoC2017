"""Day 2 basic challenge."""
import re
with open('input.txt', 'r') as f:
    data = f.readlines()

seq = []

for line in data:
    newline = re.split(' *', line)
    newline = [i.replace('\n', '') for i in newline]
    newline = [int(i) for i in newline]
    seq.append(newline)

sum = 0


def find_div(line):
    foundmatch = False
    result = 0
    for pos, number in enumerate(line):
        newline = [i for i in line if i != number]
        print(newline)
        for newnum in newline:
            if number % newnum == 0:
                result = number / newnum
                foundmatch = True
                break
        if foundmatch:
            break
    return result


for line in seq:
    sum += find_div(line)


print(sum)
