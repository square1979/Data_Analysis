import xlrd

data = xlrd.open_workbook('test.xlsx')
table = data.sheets()[0]
"""
# 返回单元格对象
print(table.cell(0, 0))
# 返回对应位置单元格中的数据类型
print(table.cell_type(0, 0))
# 返回对应位置单元格中的数据
print(table.cell_value(0, 0))
"""
num_rows = table.nrows
num_cols = table.ncols
# print(num_rows, num_cols)
for i in range(num_rows):
    for j in range(num_cols):
        print(table.cell_value(i, j), end=" ")
    print("\n")
