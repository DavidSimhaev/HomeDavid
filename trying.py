from itertools import groupby
g = [{'color': 'Черный'}, {'color': 'Черный'}]

d = list(map(lambda x: x[0] , groupby(g, key=lambda x: x["color"])  ))
print(d)


text = ['James\n', 'Peter, Paul, Mary\n','James\n']

newlist = ['James', 'Fennimore', 'Cooper\n', 'Peter', 'Paul,', 'and', 'Mary\n',
        'James', 'Gosling\n']



newlist = []

for item in text:
    newlist.extend(item.split())
    print(newlist)
    

          

