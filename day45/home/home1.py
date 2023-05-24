# проверить все ли числа последовательности уникальны
import math


l = [10,15,20,25,30,35,40,45,10,15]

if len(l) > len(set(l)):
   print("Массив неуникальный")
else:
    print("Массив уникальный")
#с помощью анонимной функции извлеките из списка все числа что делятся на 15
e = list(filter(lambda x: x%15 == 0 , l ))
print(e)
#3 сделать список списков в каждом вложенном списке n элементов и n таких списков
#  заполнить все 0

#  0 0 0
#  0 0 0
#  0 0 0

class A(): # Квадрат можно увеличить не больше 10 раз
    def __init__(self, quantity):
        self.quantity = quantity
        self.list = []
        
    def kvadrat(self): # Только нечетные!
        zero = "0"
        a = self.quantity * [zero]
        for _ in range(self.quantity):
            self.list.append(a)
            yield a
    

n = A(3)
print(next(n.kvadrat()))
print(next(n.kvadrat()))
print(next(n.kvadrat()))


try:
    if n.quantity % 2 != 0: # Здесь нужно писать после образование квадрата ещё один генератор
        n.list[len(n.list)//2][len(n.list)//2]= 1
        print(n.list)
        
except StopIteration as ex:
    print("Введите нечетное число")

