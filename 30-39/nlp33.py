from nlp30 import get_morph
from itertools import chain

morph = get_morph()
doushi = list(chain.from_iterable([[s['base'] for s in sentence if s['pos1'] == 'サ変接続']
                                   for sentence in morph]))

print(doushi)
