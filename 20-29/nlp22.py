from nlp20 import get_england
import re

str = get_england()
p = re.compile(r'\[\[Category:(.+?)\]\]')
print('\n'.join(p.findall(str)))
