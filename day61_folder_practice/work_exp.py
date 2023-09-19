def fun(x):
    assert x>=0
    return x ** 0.5

def mid_level(x):
    try:
        fun(x)
    except Error:
        raise
    
try:
    x = mid_level(-1)
except RuntimeError:
    x=-1
except:
    x=-2
print(x)

test = "lalala\ri'm back\a hello world"

print(test)

S = "в" * 0   
print(10 == "10" )

# Example

class A:
    def do(self):
        print("A")


class BL(A):
    def do(self):
        print("BL")


class BR(A):
    def do(self):
        print("BR")


class C(BR, BL):
    pass


o = C()

class ABRA:
    ATTR = 1
    
    def __init__(self,stuff):
        self.stuff = stuff
        
    def __metoooood(self):
        print(2)
g = ABRA()

