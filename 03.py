import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ls = list(map(len, re.sub('[,.]','',s).split(' ')))
print(ls)
