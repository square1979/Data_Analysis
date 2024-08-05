import pandas as pd

data = [['你好', 10], ['我好', 12], ['她好', 13]]
df = pd.DataFrame(data)
print(df)
df1 = pd.DataFrame(data, columns=['name', 'Age'])
print(df1)
