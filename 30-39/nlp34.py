from nlp30 import get_morph
from itertools import chain

morph = get_morph()
morph_flat = list(chain.from_iterable(morph))

ans = []
for i, m in enumerate(morph_flat):
    if m['surface'] == 'の' and m['pos'] == '助詞' and m['pos1'] == '連体化':
        ans.append(morph_flat[i-1]['surface'] +
                   m['surface']+morph_flat[i+1]['surface'])

print(ans)
