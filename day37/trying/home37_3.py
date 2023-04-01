"""
1) генератор(n)
x x x
x x x
x x x
где x случайное число но таких массивов будет n
сделать список загнать в numpy поменять размерность
2)генератор n случайных колод карт
3)декоратор замеряющий время выполнения функции"""




from pprint import pprint
import random
import numpy
def generator(b,n):
    l=[]
    for _ in range(n):
        a = numpy.array([random.randint(1,1000) for _ in range(1,4)])
        yield a 
    print (l)
    b-=1
    if b==0:
        return
    return generator(b, n)

h = generator(10,5)
print(next(h))
print(next(h))
print(next(h))
print(next(h))
print(next(h))
