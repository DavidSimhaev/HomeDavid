from superclassapi import GetFromApi
from itertools import groupby

url = "http://universities.hipolabs.com/"
p = {"country": "russian federation", "name": "mos" }



universits = GetFromApi(url).addMethod(method = "search").GetDataFromApi()

print(universits.GetDictionaryByParameter("country")["Israel"])