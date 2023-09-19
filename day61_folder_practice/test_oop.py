
from os import mkdir


class ABRA:
    ATTR = 1
    def __init__(self):
        self.stuff = 1
        
    def metoooood(self):
        return 2
    def p(self):
        print(ABRA.metoooood(self))
class ABRA2(ABRA):
    ATTR = 2   
g = ABRA()
r = ABRA2()

class ABRA3(ABRA):
    def metoooood(self):
        return 3
    
class ABRA_END(ABRA2, ABRA3):
    def HELLO(self):
        pass
print(isinstance(r, ABRA))



#print(ABRA3 in ABRA_END.__base__)


class A():
    
    g= 0
    
    def __init__(self, checcck) -> None:
        self.check = checcck
        
    def show_id(self):
        print(self.get_id())
        
    def get_id(self):
        return "бубубубу"
    
class B(A):
    def __init__(self, checcck) -> None:
        super().__init__(checcck)
    
    def get_id(self):
        return "лалалала"

b = B(5)
b.show_id()

print(b.g)

print(b.check)


print(str(len(b.__dict__)) + " " + str(len(B.__dict__)))

print(b.__dict__)



class test():
    stat = 4
    
    def __init__(self) -> None:
        self.atr = 2
        
    def method(self):
        pass
    

obj = test()

print(str(len(obj.__dict__)) + " " + str(len(test.__dict__)))


print(test.__dict__)

if 1 == True:
    print(555555555555555555)