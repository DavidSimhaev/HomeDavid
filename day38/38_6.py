import pandas as pd
import numpy as np
from pprint import pprint

frame = pd.DataFrame(np.arange(16).reshape(4,4),index = ['red', 'blue', 'white', 'green'], columns=['ball', 'pen', 'pencil', 'paper'])
pprint(frame)
