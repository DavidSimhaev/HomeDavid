from itertools import groupby
def mapfunc(w):
        cleanword = "".join(x for x in w if x.isalpha() or x == " ")
        return [cleanword.lower()]

with open("C:/Users/ASUS/Desktop/Pythin/day12.py/sherlok.txt") as f:
    words = [word for line in f for word in line.split()]
    
    words.sort()
    
    print(len(words))
    
    
    
   
    