# & Оба операранда должны ровняться 1 в противном случаи выдает ноль

# ^ Если один операнд равен одному выдает 1 в противном случаи 0 

3&12 # & = Ровняется 0 (3 = 0011 , 11= 1011)

2&9 # & = Ровняется 0 ( 2 = 0010, 9 = 1001 )

0^0 # Выдаст ноль

4 | 0 # Выдаст ноль (4 = 100, 0 = 0)

print(4 | 3&12 ^ 2&9)
