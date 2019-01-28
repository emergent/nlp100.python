import json
with open('jawiki-country.json') as f:
    line = f.readline()
    while line:
        d = json.loads(line) 
        if d['title'] == 'イギリス':
            print(d['text'])
        line = f.readline()

