import mysql.connector
from itertools import groupby

catdb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "098098098"
)


catcursor = catdb.cursor()
query =  'select exhibit.name, exhibit.data, exhibit.adress, cats.name, cats.age, cats.color, cat_owner.name, cat_owner.surname from predicator.cat_exhibidit_relation '
query += 'left join predicator.exhibit '
query += 'on ' 
query += 'cat_exhibidit_relation.exhibidit = exhibit.idexhibit '
query += 'left join predicator.cats '
query += 'on cat_exhibidit_relation.catid = cats.id '
query += 'left join predicator.owners_cats_relation '
query += 'on cats.id = owners_cats_relation.catid '
query += 'left join predicator.cat_owner '
query += 'on owners_cats_relation.ownerid = cat_owner.idcat_owner '

catcursor.execute(query)
cats = catcursor.fetchall()


print(cats)

# 0 - имя мероприятия 3 - имя кота


cats.sort(key = lambda x: x[0])
print(cats)

dcats = dict(map(lambda record: (record[0],list(map(lambda t: t[3], record[1]))) , groupby(cats, key = lambda x: x[0])))


print("_____")
#print(dcats)



#newcats = dict(map(
#    lambda e: (e[0], dict(map(lambda y: y[6], e[1])), groupby(e[1], key = lambda p: p[1]))
#    , groupby(cats, key = lambda x: x[0])
#))

newcats = dict(map( lambda e: (e[0], list(map( lambda p: p[3], e[1]))) , groupby(cats, key = lambda x: x[0])))
ddd = {}
for k in groupby(cats, key = lambda x: x[0]):
    ddd[k[0]] = list(map(lambda e: e[3], k[1]))
print(ddd)
print(cats)
print(newcats)


#for k in groupby(cats, key = lambda x: x[0]):
#    print(k[0], list(k[1]))
# ключ : ключ 