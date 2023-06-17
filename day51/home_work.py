import pymongo
import pandas as pd
def mapfunc(w):
    cleanword = "".join(i for i in w if i.isalpha() or i == " ")
    return [cleanword.lower(), 1]
with open("sherlok.txt", "r") as f:
    text = f.read()
    text = text.split()
map_result = list(map(mapfunc, text))   
res = pd.DataFrame(map_result).groupby([0], as_index=False)[1].sum().values.tolist()
ready = sorted(res , key = lambda x: x[1], reverse= True)
dict_ready = {ready[index][0]: ready[index][1] for index in range(len(ready)) if ready[index][1] >= 20  }
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Sherlok"] # Создание базы данных !!!!!
collection = mydb["SHERLOKHOMS"] # Создание коллекции!!!!
for key in dict_ready:
    d = {"word": key,
         "quantity": dict_ready[key]}
    collection.insert_one(d)
    