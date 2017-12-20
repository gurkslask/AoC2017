"""Day 7."""
import re
test = False
if test:
    with open('input_test.txt', 'r') as f:
        data = f.readlines()
else:
    with open('input.txt', 'r') as f:
        data = f.readlines()

#re_ptr = '^(\w*) \(.*\) -> (.*)$'
data_dict = {}
re_ptr = '^(\w*)'
re_ptr2 = '> (.*)$'
for line in data:
    # print(line)
    match = re.search(re_ptr, line)
    if match:
        key = match.group(1)
        # print(key)
        data_dict[key] = []
    match = re.search(re_ptr2, line)
    if match:
        # print(match.group(1))
        mtp = match.group(1)
        mtp = mtp.replace(' ', '')
        mtp = mtp.split(',')
        data_dict[key] = mtp

print(data_dict)

for key in data_dict:
    right = False
    breakl = False
    # print(key)
    for ikey in data_dict:
        if ikey != key:
            # if not the same
            if key in data_dict[ikey]:
                breakl = True
        if breakl:
            break
    if not breakl:
        print(key)
                
