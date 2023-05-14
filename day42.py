l =[]
for i in range(12):
    l.append(i)
    
    
print(l)


l = {"a": 10, "b":11, "c":12, "d":13}


b = l.items()
print(b)

d = dict(map( lambda x : (x[1], x[0] )  ,b))

print(d)

c = dict((y,x) for x , y in l.items() )
print(c)
a = ["a", "b", "c"]

r = dict(filter( lambda x: x[0] in a, l.items()))
print(r)