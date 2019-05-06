import requests
import json

url = "https://ja.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "ファイル:Flag_of_the_United_Kingdom.svg"
}

r = requests.get(url, params=params)
j = r.json()

filename = j['query']['pages']['-1']['title']

print("https://ja.wikipedia.org/wiki/{}".format(filename))
