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

for line in seq:
    imax = max(line)
    imin = min(line)
    sum += imax-imin

print(sum)
