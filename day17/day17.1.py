import requests
from itertools import groupby
url = "http://universities.hipolabs.com/search?country"
headers = {'Accept': 'application/json'}



r = requests.get(url = url, headers=headers)

universits = list(r.json())
countries = list(map(lambda x: x["country"], universits))
countries.sort()



print(countries)