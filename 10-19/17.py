with open('hightemp.txt') as f:
    data = map(lambda s: s.split('\t')[0], f.readlines())
    print(set(data))
