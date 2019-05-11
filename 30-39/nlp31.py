from nlp30 import get_morph
from itertools import chain

morph = get_morph()
doushi = list(chain.from_iterable([[s['surface'] for s in sentence if s['pos'] == '動詞']
                                   for sentence in morph]))

print(doushi)
