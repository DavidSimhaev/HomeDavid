from file import fileOperator
from itertools import groupby
fo = fileOperator('localhost','root','098098098')
print(fo.getData())
query = 'SELECT * FROM Predicator.Finances;' # Запрос



# Изначальный результат
result = fo.setQuery(query).getData()             #print(result)


def remap( grouplist ): # Функция создающяя лист из значений года
    l = []
    group = list(grouplist) # group создает лист 
    for t in group:
        l.append((t[1],t[2],t[3])) 
    return l    # Возращает по индексам список, который -
#                                       берется отсюда  - 
#                      (Ключ года)(Лист значений)--------                                                        
d = dict(map( lambda y: (y[0],  remap(y[1])), # Который имеет первый индекс от d - словаря!
        groupby(result, key=lambda x: x[0])
    )                  # Групировка по нулевому индексу(год)      
)



def remapd ( grouplist): # Функция создающяя лист в словаре из значений месяца!
    l = []
    group = list(grouplist) # Group создает лист значений из месяцов
    for k in group:
        l.append((k[1:]))
    return l



q = dict(map(lambda y: (y[0], remapd(y[1])),groupby(result, key=lambda x: x[0])))
print(q)
print("Я тут")


# Правильная версия учителя 

#print(result)




d = dict(
    map(
        lambda y: (y[0],  dict(
            map(
                lambda z: (z[0],  dict(
                    map(lambda q: (q[2],q[3]), z[1]))),
                        groupby(y[1], key=lambda p: p[1])
            )
        )),
        groupby(result, key=lambda x: x[0])
    )
)
print(d)


bestyaer = ["0",0]
print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-")

def yearincome(fin, year):
    sum = 0.0
    for month in fin[year]:
        for business in fin[year][month]:
            sum = sum + fin[year][month][business]
    return sum

for year in d:
    t = yearincome(d, year)
    if t > bestyaer[1]:
        bestyaer = [year, t]
print(bestyaer, "Сумма за весь год")

def bestmount (fin, year):
    max = (year,"", 0,0)
    for mount in fin[year]:
        sum = 0.0
        for business in fin[year][mount]:
            sum = sum + fin[year][mount][business]
        if sum > max[2]:
            max = [year, mount, sum]
    return max

for year in d:
    print((bestmount(d, year)))













#for key2 in q:
#    for i in q[key2]:
            
#print(q)
#for key in q:
    #print(q[key])
    #q[key] = dict(map(lambda x: (x[0], remapd(x[1])),groupby(q[key], key=lambda x: x[0])))
        



# найти в каждом году лучший месяц по доходам
#money = []
#money.append(sum(ll[0:36]))
#money.append(sum(ll[36:72]))
#money.append(sum(ll[72:108]))
#money.append(sum(ll[108:144]))
#money.append(sum(ll[144:180]))

#print(money)


#t = ""
#for i in money:
#    if i == max(money):
#        for f in range(len(money)):
#            if f == money.index(max(money)):
#                print()