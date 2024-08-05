import pandas as pd
from pandas import Series

data = {1: 'jack', 2: 'json', 3: 'may', 4: 'what'}
var = Series(data, index=[1, 3])
# var1 = Series(data, index=['x', 'y'])
print(var)
# print(var1)
