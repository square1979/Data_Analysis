"""
四种空数据：n/a   NA  —   na 替换为NAN
missing_values = ["n/a", "na","--"]
df = pd.read_csv('property-data.csv',
na_values = missing_values)
"""
import pandas as pd

df = pd.read_csv('property-data.csv')
# 默认情况下，dropna() ⽅法返回⼀个新的DataFrame，不会修改源数据。
# 如果你要修改源数据 DataFrame, 可以使⽤ inplace = True 参数
df1 = df.dropna()
df2 = df.dropna(inplace=True)
# 移除 ST_NUM 列中字段值为空的⾏
df.dropna(subset=['ST_NUM'], inplace=True)
# fillna() ⽅法来替换⼀些空字段：
df.fillna(12345, inplace=True)
# 指定某⼀个列来替换数据,使⽤ 12345 替换 PID 为空数据
df['PID'].fillna(12345, inplace=True)
