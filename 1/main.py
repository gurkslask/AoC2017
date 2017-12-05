"""blablabla."""
with open('s.txt', 'r') as f:
    data = f.read()

# print(data)
data = data.replace('\n', '')
seq = [int(i) for i in data]
sum = 0
last = 0

for num in seq:
    # print(num)
    if num == last:
        sum += num
    last = num

if seq[-1] == seq[0]:
    sum += seq[0]

print(sum)
