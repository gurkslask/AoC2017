"""Day 7."""
import re
test = True
if test:
    with open('input_test.txt', 'r') as f:
        data = f.readlines()
    begin = 'tknk'
else:
    with open('input.txt', 'r') as f:
        data = f.readlines()
    begin = 'hlhomy'


def find_the_odd(dikt, key):
    countdict = {}
    for member in dikt[key]['members']:
        try:
            countdict[dikt[member]]['count'] += 1
            countdict = {}
        except KeyError:
            countdict[dikt[members]] = {'count': 1, 'member': []}
        countdict[dikt[members]]['member'].append(member)
    for key in countdict:
        if countdict[key]['count'] == 1:
            print(countdict[key]['member'])


data_dict = {}
re_ptr = '^(\w*) \((\d*)\)'
re_ptr2 = '> (.*)$'
for line in data:
    # print(line)
    match = re.search(re_ptr, line)
    if match:
        key = match.group(1)
        # print(key)
        data_dict[key] = {'weight': match.group(2), 'members': None}
    match = re.search(re_ptr2, line)
    if match:
        # print(match.group(1))
        mtp = match.group(1)
        mtp = mtp.replace(' ', '')
        mtp = mtp.split(',')
        data_dict[key]['members'] = mtp

# print(data_dict)

print(data_dict[begin])
find_the_odd(data_dict, begin)

