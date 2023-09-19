import platform

print(platform.machine())
print(platform.platform())
print(platform.processor())
print(platform.system())
print(platform.version())

import tkinter.ttk



import random


print(random.random())

import random

print(random.randrange(100))
print(random.randrange(0,100))
print(random.randrange(0,100,1))
import sys
print(sys.path)


x, y = 1, 0
try:
    value = int(input("Enter value: "))
    print("Reciprocal of the value is", 1 / value)
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("An unidentified exception")
else:
    print("Success")
finally:   
    print("Completed")
    
    
try:
    value = float(input("Enter value: "))
    print(2 / value)
    print(2 ** value)
except ZeroDivisionError:
    print("more specialized")
except ArithmeticError:
    print("more general")
except:
    print("other")
else:
    print("success")

# Example


s = "test string"
try:
    s = s[100]
except Exception as exc:
    print(exc)


print(ArithmeticError)
print(ArithmeticError.__subclasses__())

try:
    raise ZeroDivisionError
except Exception as exc:
    print(exc.args)
try:
    raise ZeroDivisionError(2, "nd exception")
except Exception as exc:
    print(exc.args)
    
class RangeError(IndexError):

    __errors = 0

    def __init__(self, the_index):
        IndexError.__init__(self, "erroneous index: " + str(the_index))
        RangeError.__errors += 1

    def get_error_counter(self):
        return RangeError.__errors


class Collection:
    def get(self, index):
        if not (1 <= index <= 10):
            raise RangeError(index)
        return 42


stuff = Collection()
for _ in range(2):
    try:
        print(stuff.get(1))
        print(stuff.get(0))
    except RangeError as error:
        print("failure")
        print(error)
        print(error.get_error_counter())
        
        
print(314e-2)