with open('col1.txt') as f1:
    data1 = f1.read().strip().split('\n')

with open('col2.txt') as f2:
    data2 = f2.read().strip().split('\n')

print('\n'.join(map('\t'.join, zip(data1, data2))))
