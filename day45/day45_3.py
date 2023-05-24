from typing import Any
import random

class B:
    def __call__(self) -> Any:
        return random.randint(1,200)
    
b = B()
print(b)

b.value = 6
print(b.value)
B.value=7
print(B.value)
print(b()) # обращение объекта b через __call__
print(b())# обращение объекта b через __call__
print(b())# обращение объекта b через __call__
print(B()) # Объект класс 

print(type(type))
print(type(B))