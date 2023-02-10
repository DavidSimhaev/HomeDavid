from itertools import groupby
g = [{'color': 'Черный'}, {'color': 'Черный'}]

d = list(map(lambda x: x[0] , groupby(g, key=lambda x: x["color"])  ))
print(d)