from itertools import groupby


def mapfunc(w):
    cleanword = "".join(i for i in w if i.isalpha() or i == " ")
    return [cleanword.lower(), 1]


def reducefunc(key, values):
    return [key, len(values)]


with open("C:/Users/ASUS/Desktop/Pythin/day12.py/sherlok.txt") as f:
    words = [word for line in f for word in line.split()]


map_result = list(map(mapfunc, words))

map_result_sorted = sorted(map_result, key=lambda x: x[0])

reduce_result = []
for k, g in groupby(map_result_sorted, key=lambda x: x[0]):
    reduce_result.append(reducefunc(k, list(g)))
print(len(reduce_result))
