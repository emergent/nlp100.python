import random
def typoglycemia(word):
    if len(word) <= 2:
        return word
    else:
        center = list(word[1:-1])
        random.shuffle(center)
        return word[0] + ''.join(center) + word[-1]

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(' '.join(map(typoglycemia, s.split(' '))))
