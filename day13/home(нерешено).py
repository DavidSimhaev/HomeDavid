f1 = 1
f2 = 1

n = int(input())

# print(f1,f2, end = " ")

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=" ")

while f2 < 2:
    print(f2, end=" ")
    f1, f2 = f2, f1 + f2


from keras import *
from keras import layers
from tensorflow import *

# создаете массив для теста и проверок например числа фибоначчи и тренируете нейросеть для предсказания

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Число n
output = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
