import datetime
from functools import reduce
from random import randint
from itertools import combinations
  
l = [[2, 8, 9, 3, 1, 11, 12],    # 1 - index 0 1
     [2, 4, 6, 3, 4, 1, 3, 4],   # 2 - index 1 1,2 
     [1, 3, 14, 15, 16, 17],     # 3 - index 2 1,2,3
     [1, 2, 3, 4],               # 4 - index 3 1,2,3,4
     [3, 4, 5],                  # 5 - index 4 1,2,3,4,5
     [1, 2, 3, 4, 5, 6,7]]      # 6 - index 5 1,2,3,4,5,6



p = set(l[0])
for i in range (1, len(l)):
     p = set(l[i])&p
print(p)

t = [1,2,3,4,5,6,7,8]
ll = lambda x,y: x+y

r = reduce(lambda x,y: x+y , t)

print(r)