
list1= [10,2,3,4,5,6,7]
def func():
    for i in list1:
        yield i
        
g = func()

print(next(g))
print(next(g))
print(next(g))


