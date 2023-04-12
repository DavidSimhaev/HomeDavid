from pprint import pprint
import pandas as pd
import numpy as np

s = pd.Series([-12, 3, 4, 23], index=['a', 'b', 'c', 'd'])
pprint(s)
pprint(s.values)
pprint(s.index)

print(s['b':'d'])
print(s[2])

s[2] = 12
s['c'] = 14
print("--------")
pprint(s[s > 0])
print("Я тут")
pprint(s/2)
pprint(np.log(s))


a = 0.5 
b = np.exp(8.9)
print (np.log(a))
print (np.log(b))