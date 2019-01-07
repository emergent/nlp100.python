import sys
N=int(sys.argv[1])
with open('hightemp.txt') as f:
    data = f.readlines()

perline = len(data)//N
for i in range(0,N):
    with open('sp{:02}.txt'.format(i+1),mode='w') as fo:
        if i < N - 1:
            out = data[perline*i:perline*(i+1)]
        else:
            out=data[perline*i:]
        fo.write(''.join(out))

