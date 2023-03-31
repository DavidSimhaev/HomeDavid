"""
генератор(n)
х х х 
х х х
х х х
где х случайное число но таких массивов будет n
сделать список загнать в numpy поменять размерность

генератор n случайных колод карт

декоратор замеряющий время выполнения функции"""
from pprint import pprint
import random
import numpy
def generator(n):
    for _ in range(n):
        a = numpy.array([random.randint(1,1000) for _ in range(1,4)])
        b = numpy.array([random.randint(1,1000) for _ in range(1,4)])
        c = numpy.array([random.randint(1,1000) for _ in range(1,4)])
        
        pprint([a,b,c])


generator(5)


