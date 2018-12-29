def word_ngram(s, n=2):
    ls = s.split(' ')
    return [ls[i:i+n] for i, v in enumerate(ls)][:-1]

def char_ngram(s, n=2):
    s = s.replace(' ', '')
    return [s[i:i+n] for i, v in enumerate(s)][:-1]

print(word_ngram('I am an NLPer', 2))
print(char_ngram('I am an NLPer', 2))
