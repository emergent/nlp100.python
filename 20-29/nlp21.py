from nlp20 import get_england

str = get_england()
lines = str.split('\n')
cat_lines = '\n'.join(filter(lambda s: '[[Category:' in s, lines))
print(cat_lines)
