from nlp30 import get_morph
from itertools import chain

morph = list(chain.from_iterable(get_morph()))

ans = []
buf = []
for i, m in enumerate(morph):
    if m['pos'] == '名詞':
        buf.append(m['surface'])
    elif len(buf) > 1:
        ans.append(''.join(buf))
        buf.clear()
    else:
        buf.clear()

print(ans)
