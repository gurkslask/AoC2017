
with open('input.txt', 'r') as f:
    data = f.readlines()


data = [int(i.replace('\n', '')) for i in data]

pos = 0
done = False
i = 0

while not done:
    try:
        steps = data[pos]
        data[pos] += 1
        pos += steps
        i += 1
    except IndexError:
        print(i)
        done = True
