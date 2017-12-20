"""Meh mehasd."""
with open('input_bak.txt', 'r') as f:
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
list_of_second_results = []
iterations = 0
second_iterations = 0
found_first = False
found_second = False
repeated_sequence = ''


done = False

while not done:
    iterations += 1
    if found_first:
        second_iterations += 1
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
    if bankstr == repeated_sequence:
        print('DONE!!!')
        print(second_iterations)
        done = True
    if bankstr in list_of_results and not found_first:
        found_first = True
        repeated_sequence = bankstr
        print(repeated_sequence)


    # print(bankdict)
    list_of_results.append(bankstr)
    if found_first:
        list_of_second_results.append(bankstr)
