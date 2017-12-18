with open('input.txt', 'r') as f:
    data = f.read()

datalist = data.replace('\n', '').split('\t')
datalist = [int(i.replace('\t', '')) for i in datalist]
bankdict = {}
number_of_keys = 0
for key, value in enumerate(datalist):
    bankdict[key] = value
    number_of_keys += 1
print(bankdict)
print('This many keys:', number_of_keys)
list_of_results = []
iterations = 0


done = False

while not done:
    act_key = 0
    highest = max(bankdict.values())
    # print('Highest:', highest)

    for key in bankdict:
        if bankdict[key] == highest:
            act_key = key
            break

    # print('Actkey:', act_key)

    amount = bankdict[act_key]
    bankdict[act_key] = 0

    for i in range(amount):
        i += 1
        # print(i)
        if act_key + i not in bankdict.keys():
            i = i - number_of_keys
            if act_key + i not in bankdict.keys():
                i = i - number_of_keys
        bankdict[act_key+i] += 1

    bankstr = str(bankdict)
    if bankstr in list_of_results:
        print('DONE!!!')
        print(iterations)
        done = True

    print(bankdict)
    iterations += 1
    list_of_results.append(bankstr)
    # print(list_of_results)


