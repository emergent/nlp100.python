def char_ngram(s, n=2):
    s = s.replace(' ', '')
    return [s[i:i+n] for i, v in enumerate(s)][:-1]

X = set(char_ngram("paraparaparadise"))
Y = set(char_ngram("paragraph"))

print('X: {}'.format(X))
print('Y: {}'.format(Y))
print('X|Y: {}'.format(X | Y))
print('X&Y: {}'.format(X & Y))
print('\'se\' in X? : {}'.format('se' in X))
print('\'se\' in Y? : {}'.format('se' in Y))
