import xlrd

data = xlrd.open_workbook('test.xlsx')
table = data.sheets()[2]
print(table.col(0))
# 获取列表的有效列数
num_col = table.ncols
print(num_col)

# 返回由该列中所有的单元格对象组成的列表
col0 = table.col(0, start_rowx=0, end_rowx=None)
col1 = table.col(1, start_rowx=0, end_rowx=None)
print(col0)
print(col1)
print("---------------------------")

for i in range(num_col):
    print(table.col(i, start_rowx=0, end_rowx=None))
    # 返回由该列中所有的单元格对象组成的列表
    print(table.col_slice(i, start_rowx=0, end_rowx=None))
    # 返回由该列中所有单元格的数据组成的列表
    print(table.col_values(i, start_rowx=0, end_rowx=None))
    print("*********************")
