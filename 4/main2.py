with open ('input.txt', 'r') as f:
    data = f.readlines()

data = [i.replace('\n', '') for i in data]
print(data)

sum = 0

for line in data:
    valid = True
    lista = []
    newline = line.split(' ')
    for word in newline:
        dicta = {}
        for char in word:
            try:
                dicta[char] += 1
            except KeyError:
                dicta[char] = 1
        if dicta in lista:
            print(word)
            valid = False
        lista.append(dicta)
    print('Valid!')
    if valid:
        sum += 1
print(sum)
