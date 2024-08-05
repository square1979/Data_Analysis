"""
pandas.Series( data, index, dtype, name, copy)
    data：⼀组数据(ndarray 类型)。
    index：数据索引标签，如果不指定，默认从 0 开始。
    dtype：数据类型，默认会⾃⼰判断。
    name：设置名称。
    copy：拷⻉数据，默认为 False。
"""
import pandas as pd

data = ['迪丽热巴', '古力娜扎', '孟子义']

var = pd.Series(data)
# print(var[0])
# 设置特定索引
var1 = pd.Series(data, index=['a', 'b', 'c'])
print(var1['a'])
