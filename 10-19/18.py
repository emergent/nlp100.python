with open('hightemp.txt') as f:
    data = map(lambda s: s.strip().split('\t'), f.readlines())
    print('\n'.join(map('\t'.join, sorted(data, key=lambda l: l[2]))))
