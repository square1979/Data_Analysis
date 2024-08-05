import pandas as pd

# 使用ndarray创建
data = {
    'name': ['di', 'hi', 'hello'],
    'age': [11, 21, 31]
}
# 使用字典创建
data1 = [
    {'name': 'di', 'age': 11, 'sex': True},
    {'name': 'hello', 'age': 12, 'sex': True},
    {'name': 'may', 'sex': False}
]
data2 = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# Pandas 可以使⽤ loc 属性返回指定⾏的数据，如果没有设置索引
# 第⼀⾏索引为 0，第⼆⾏索引为 1

df = pd.DataFrame(data, index=['a', 'c', 'b'])
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df)
print(df1)
print(df2)
# 打印第二行
# print(df2.loc[1])
# print(type(df2.loc[1]))
# 也可以返回多⾏数据，使⽤ [[ ... ]] 格式，... 为各⾏的索引，以逗号隔开
print(df2.loc[[0, 1]])
# print(type(df2.loc[[0, 1]]))
# 重设索引值
df3 = pd.DataFrame(data2, index=['a', 'c', 'b'])
print(df3)
print(df3.loc['c'])
