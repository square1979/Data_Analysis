import pandas as pd

person = {
    "name": ['dylib', 'lucky', 'glen'],
    "age": [50, 40, 12345]
    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)
print(df)

"""
df.loc[2, 'age'] = 30  # 修改数据
print(df.to_string())
"""
# 设置条件语句：将 age ⼤于 20 的设置为 20.
# for x in df.index:
#     if df.loc[x, "age"] > 20:
#         df.loc[x, "age"] = 20
# print(df.to_string())

# 将 age ⼤于 120 的删除:
for x in df.index:
    if df.loc[x, "age"] > 120:
        df.drop(x, inplace=True)
print(df.to_string())
