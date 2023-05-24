from typing import Any


class A():
    
    def __init__(self) -> None:
        self.a = 5
        self.b = 8
        
    def __call__(self, x=2) -> Any:
        print(f"Call call method with parameter {x}")
        
    def sum(self):
        return self.a + self.b
    
class B(A):
    
    def __init__(self) -> None:
        super().__init__()
        self.c = 9
        
    def sum(self): # Метод переопределение 
        return super().sum()+self.c
        
a = A()
b = B()

print(b.sum()) # Понял
print(b.b) # Понял
print(b.c) # Понял
a() # Понял
b(6) # Понял