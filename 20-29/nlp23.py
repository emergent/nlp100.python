from nlp20 import get_england
import re

str = get_england()
lines = str.split('\n')
p = re.compile(r'^(=+)\s*(.+?)\s*=+')

for l in lines:
    m = re.search(p, l)
    if m is not None:
        level = len(m.group(1)) - 1
        print(m.group(2), level)
