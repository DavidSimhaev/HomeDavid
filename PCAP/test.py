class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
import math
print(math.pow(2,3))
print(int(True))

print('dsd fdfsf dfs'.title())
g  = [2 ** x for x in range(5)]
print('sdas gdf \nhell '.split())

print('100'=='0100')
l =[]
for i in '0100':
    l.append(ord(i))
print(l)
g = []
for i in '100':
    g.append(ord(i))
    
import platform

print(platform.python_implementation())




try:
    raise KeyboardInterrupt
except NameError:
    print(144)
except KeyboardInterrupt:
    print(123123123)

import os
print('gdsad'!=10)
print('ddasdsadas DS sddsa'.index('DS'))

A,B = (6,5)

print('A2wdasdw4s'.isalnum())
print(math.sqrt(25))
print(ord('a'))


class test_1():
    def __init__(self) -> None:
        self.param = 11
    def met():
        pass
bfunck = test_1.met
print(bfunck.__name__)
    
class test_2(test_1):
    def __init__(self) -> None:
        super().__init__()
        
'dasasd'
'sadasd'
'dsadsa'

l = [i for i in range(0, -5)]

print(math.sqrt(int('25')))

def ex_test():
    
    try:
        100/0
    except:
        return 1
    finally:
        return 2
    
print(ex_test())
print('dfsfsefds'.replace('','rrr'))
print(math.hypot(3.0))

try:
    2/0
except (ZeroDivisionError, Exception) as a:
    print(2323) 