from nlp30 import get_morph
from itertools import chain

morph = list(chain.from_iterable(get_morph()))

freq = {}
for m in morph:
    f_m = freq.get(m['surface'], 0)
    freq[m['surface']] = f_m + 1

ans = list(freq.items())
ans.sort(key=lambda x: x[1], reverse=True)
print(ans)
