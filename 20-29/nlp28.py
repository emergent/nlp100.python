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

subp = re.compile(r'\[\[(?:[^\]\|]+?\|){0,2}(.+?)\]\]')
for k in kiso:
    val = kiso[k].replace(r"'", '')
    val = re.sub(subp, r'\1', val)
    val = re.sub(r'<ref.*?>(?:.|\s)+?<\/ref>', '', val)
    val = re.sub(r'<.*?\/>', '', val)
    val = re.sub(r'{{\w+?\|\w+?\|(.+?)}}', r'\1', val)
    kiso[k] = val

for k, v in kiso.items():
    print(k, v)
