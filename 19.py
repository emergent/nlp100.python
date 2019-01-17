from collections import Counter

with open('hightemp.txt') as f:
    data = map(lambda s: s.split('\t')[0], f.readlines())
    c = Counter(data)
    print('\n'.join(map(lambda s: s[0], sorted(c.items(), key=lambda x: x[1], reverse=True))))
