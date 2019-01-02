with open('hightemp.txt') as f:
    data = map(lambda s: s.split('\t'), f.readlines())

with open('col1.txt', mode='w') as fo1:
    fo1.writelines(map(lambda l: l[0]+'\n', data))

with open('col2.txt', mode='w') as fo2:
    fo2.writelines(map(lambda l: l[1]+'\n', data))

