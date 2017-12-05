num = 1
x = 0
y = 0
done = False
seq = 2
# ans = 1024
ans = 347991
i = 0

def checknum(num, x, y):
    if num == ans:
        print(x , y)
        return True
    return False

while not done:
    x += 1
    num += 1
    if not done: done = checknum(num, x, y)
    for i in range(seq - 1):
        y += 1
        num += 1
        # print('num: {}, x: {}, y: {}'.format(num, x, y))
        if not done: done = checknum(num, x, y)
    for i in range(seq):
        x -= 1
        num += 1
        # print('num: {}, x: {}, y: {}'.format(num, x, y))
        if not done: done = checknum(num, x, y)
    for i in range(seq):
        y -= 1
        num += 1
        # print('num: {}, x: {}, y: {}'.format(num, x, y))
        if not done: done = checknum(num, x, y)
    for i in range(seq):
        x += 1
        num += 1
        # print('num: {}, x: {}, y: {}'.format(num, x, y))
        if not done: done = checknum(num, x, y)
    print('num: {}, x: {}, y: {}'.format(num, x, y))
    seq += 2
    i += 1
    if i == 3:
        done = True

print('done!')
