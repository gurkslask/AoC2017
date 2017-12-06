num = 1
x = 0
y = 0
done = False
seq = 2
# ans = 1024
ans = 347991
i = 0
matrix = {'0:0': 1}

def checknum(num, x, y):
    if num > ans:
        print('answer:', num)
        return True
    return False


def addToMatrix(num, x, y, matrix): 
    # matrix = dict{'x:y'}
    matrix['{}:{}'.format(x, y)] = num
    return matrix


def checkMatrix(x, y, matrix):
        try:
            return matrix['{}:{}'.format(x, y)]
        except KeyError:
            return 0

def sumMatrix(x, y, matrix):
    sum = 0
    sum += checkMatrix(x+1, y, matrix)
    # print('summa:', sum)
    sum += checkMatrix(x-1, y, matrix)
    # print('summa:', sum)
    sum += checkMatrix(x+1, y+1, matrix)
    # print('summa:', sum)
    sum += checkMatrix(x-1, y-1, matrix)
    # print('summa:', sum)
    sum += checkMatrix(x, y+1, matrix)
    # print('summa:', sum)
    sum += checkMatrix(x, y-1, matrix)
    # print('summa:', sum)
    sum += checkMatrix(x+1, y-1, matrix)
    # print('summa:', sum)
    sum += checkMatrix(x-1, y+1, matrix)
    # print('summa:', sum)
    return sum

while not done:
    x += 1
    num = sumMatrix(x, y, matrix)
    matrix = addToMatrix(num, x, y, matrix)
    # print('num: {}, x: {}, y: {}'.format(num, x, y))
    # print(matrix)
    if not done:
        done = checknum(num, x, y)
    for i in range(seq - 1):
        y += 1
        num = sumMatrix(x, y, matrix)
        matrix = addToMatrix(num, x, y, matrix)
        # print('num: {}, x: {}, y: {}'.format(num, x, y))
        # print(matrix)
        if not done:
            done = checknum(num, x, y)
    for i in range(seq):
        x -= 1
        num = sumMatrix(x, y, matrix)
        matrix = addToMatrix(num, x, y, matrix)
        # print('num: {}, x: {}, y: {}'.format(num, x, y))
        # print(matrix)
        if not done:
            done = checknum(num, x, y)
    for i in range(seq):
        y -= 1
        num = sumMatrix(x, y, matrix)
        matrix = addToMatrix(num, x, y, matrix)
        # print('num: {}, x: {}, y: {}'.format(num, x, y))
        # print(matrix)
        if not done:
            done = checknum(num, x, y)
    for i in range(seq):
        x += 1
        num = sumMatrix(x, y, matrix)
        matrix = addToMatrix(num, x, y, matrix)
        # print('num: {}, x: {}, y: {}'.format(num, x, y))
        # print(matrix)
        if not done:
            done = checknum(num, x, y)
    print('num: {}, x: {}, y: {}'.format(num, x, y))
    seq += 2
    i += 1
    if i == 1:
        done = True

print('done!')
