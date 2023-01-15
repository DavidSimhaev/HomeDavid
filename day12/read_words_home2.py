
from datetime import datetime
from itertools import groupby
print('start ',datetime.now())

with open("C:/Users/ASUS/Desktop/Pythin/day12.py/sherlok.txt", encoding="utf-8") as f:
    fulltext = f.read()
    fulltext = "".join([x for x in fulltext if x.isalpha() or x == " "])
    fulltext = fulltext.lower()
    ls = fulltext.split()
    print('get words',datetime.now())
    unique = set(ls)
    print("get unique", datetime.now())
    d = dict()
    print("________________")
    
    print(len(ls), "Всего слов")
    print(len(unique), "Уникальных слов")  
    for word in unique:
        d[word] = ls.count(word)
    print(len(ls))
    print(len(unique))  

d = dict(sorted(d.items(), key= lambda x: x[1], reverse= True))





