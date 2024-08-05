import pandas as pd

df = pd.read_excel('test.xlsx')
# print(df)
# 平均数
# mean = df['lucky'].mean()
# print(mean)
# df["lucky"].fillna(mean, inplace=True)
# print(df.to_string())

# 中位数
# median = df['lucky'].median()
# print(median)
# df["lucky"].fillna(median, inplace=True)
# print(df.to_string())

mode = df['lucky'].mode()
print(mode)
df["lucky"].fillna(mode, inplace=True)
print(df.to_string())

