import json


def get_england():
    ret = ''
    with open('jawiki-country.json') as f:
        line = f.readline()
        while line:
            d = json.loads(line)
            if d['title'] == 'イギリス':
                ret = d['text']
                break
            line = f.readline()
    return ret


if __name__ == '__main__':
    print(get_england())
