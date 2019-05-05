import sys
N=int(sys.argv[1])
with open('hightemp.txt') as f:
    print(''.join(f.readlines()[-N:]))
