with open ('input.txt', 'r') as f:
    data = f.readlines()

data = [i.replace('\n', '') for i in data]
print(data)

sum = 0

for line in data:
    valid = True
    a = {}
    newline = line.split(' ')
    for word in newline:
        try:
            a[word] += 1
        except KeyError:
            a[word] = 1
    for key in a:
        if a[key] >= 2:
            print('Invalid!')
            valid = False
            break
    print('Valid!')
    if valid: sum += 1
print(sum)

