import pandas as pd

# 读取excel文件
df = pd.read_excel('test.xlsx')
# print(df)
# 打印数据前五行
print(df.head())
# 打印数据后五行
print(df.tail())
# 打印全部数据
print(df.to_string())
# 写入excel文件中
# df.to_excel('test010.xlsx', index=True)
"""
参数的使用
常⽤参数
    index 是否写⼊索引 默认为True
    header 是否写⼊表头 默认True
    sheet_name 写⼊哪个sheet⻚ 默认sheet1
    startrow 写⼊Excel数据开始⾏ 默认0⾏
    startcol 写⼊Excel数据开始列 默认0列
"""
df1 = pd.read_excel('test.xlsx', header=None)
print(df1)
# # 写⼊Excel 去除表头和索引
df1.to_excel('test-header.xlsx', index=False, header=False)
