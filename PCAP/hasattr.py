import platform

print(platform.platform(aliased=0, terse=0))


class Spam:
    __ham, ham = "__ham", "ham"
    def __method(self):
        pass
    eggs = __method
s = Spam()

print(s.__module__)
print(Spam.__module__)
print(s.eggs.__module__)

import os

print(os.name)

print("reee   "+"hellooooo.com] ".rstrip('com'))
print(__name__)
print(s.__module__)
print(Spam.__module__)
print(s.eggs.__module__)



class TEST:
    def __init__(self) -> None:
        print(123)
    def dsa():
        pass
    

class TEST2(TEST):
    def __init__(self) -> None:
        print(456)

class TEST3(TEST2):
    pass

G = TEST3()


        
b = bytearray()
print(b)

from datetime import time

f= "abc".join("123")

t= "ABCD"

import platform

print(type(platform.version()))
from calendar import calendar

import math, cmath


def main():
    
    x = 10 
    list = [x, 20,30]
    
    def iner():
        x = 50
        list[0]  = x
        return
    iner()
    print(x, list)
    
main()
class y(object):
    pass    
g = "dfdfsd".isdigit
    
import math

print(math.factorial(3))

g=  '' in 'ssfdssa'

g = hasattr(y , 'myvar')
print(os.system(""))
assert(False)
