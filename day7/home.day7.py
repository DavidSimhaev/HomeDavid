from itertools import groupby

input = [
    ("11013331", "JUN", "2002"),
    ("9085267", "MAY", "2002"),
    ("5238761", "JLY", "2005"),
    ("5349618", "JLY", "2003"),
    ("11788544", "JUN", "2005"),
    ("962142", "JLY", "2002"),
    ("7795297", "MAY", "2003"),
    ("7341464", "JLY", "2004"),
    ("9843236", "MAY", "1998"),
    ("5594916", "MAY", "1999"),
    ("1550003", "MAY", "2001"),
]
input.sort(key=lambda x: x[2])
for x in range(0, len(input)):  # запомнить!
    print(input[x])


d = {key: [v[0] for v in group] for key, group in groupby(input, key=lambda x: x[2])}
print(d)
print("______________________")


for key, value in d.items():
    print(f"key = {key} value = {value}")


# Отсортировать по годам
# Отсортировать по месяцам

# сортируем по годам
# группируем по годам
##{
#    year: {
#        month: sum
#    }
# }
