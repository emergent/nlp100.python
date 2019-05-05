from nlp20 import get_england
import re

str = get_england()
lines = str.split('\n')[2:59]

p = re.compile(r'^\|(.+)\s+=\s+(.+)$')
kiso = {}
lastkey = ''
for l in lines:
    m = p.search(l)
    if m is not None:
        lastkey = m.group(1)
        kiso[lastkey] = m.group(2)
    else:
        kiso[lastkey] = kiso[lastkey] + '\n' + l

for k, v in kiso.items():
    print(k, v)
