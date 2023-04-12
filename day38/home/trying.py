import pandas as pd
import numpy as np
from pprint import pprint

frame = pd.DataFrame(np.arange(16).reshape(4,4),index = ['red', 'blue', 'white', 'green'], columns=['ball', 'pen', 'pencil', 'paper'])

s1 = frame.iloc[:3]
s2 = frame.iloc[[2],[0,2]]
print(s2)
pprint(frame.axes[1])


a = [1,2,1,4]
b = [4,1,1,2]
c = [1,1,1,4]

def eq_elements(x,y):
    if len(x) != len(y): return False
    for z in y:
        try:
            x.remove(z)
        except:
            return False
    return True

rez = eq_elements(a[:],b)

print (f"lists elements  is {'' if rez else 'not' } equal ")
