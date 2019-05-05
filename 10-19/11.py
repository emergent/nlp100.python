with open('hightemp.txt') as f:
    data = f.read().strip()

print(data.replace('\t', ' '))
