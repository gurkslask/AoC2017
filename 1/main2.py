"""This is the harder one."""
with open('s.txt', 'r') as f:
    data = f.read()

# print(data)
data = data.replace('\n', '')
seq = [int(i) for i in data]
sum = 0
halfway_num = 0
seq_len = int(len(seq) / 2)
print(seq_len)

for pos, num in enumerate(seq):
    # print(num)
    if pos+1 > seq_len:
        halfway_num = seq[pos-seq_len]
        d = pos
    else:
        halfway_num = seq[pos+seq_len]
        d = pos+seq_len
    print(d)
    if num == halfway_num:
        sum += num

# if seq[-1] == seq[0]:
    # sum += seq[0]

print(sum)
