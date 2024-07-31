import xlrd

data = xlrd.open_workbook('test.xlsx')
table = data.sheets()[2]
print(table)

# 获取该sheet中的⾏数，注，这⾥table.nrows后⾯不带().
num_rows = table.nrows
print(num_rows)

# 返回由该⾏中所有的单元格对象组成的列表,这与tabel.raw()⽅法并没有区别。
print(table.row(2))
print("---------------------------")
# 每一行进行输出
for i in range(num_rows):
    print(table.row(i))
    # 返回由该⾏中所有的单元格对象组成的列表
    print(table.row_slice(i))
    # 返回由该⾏中所有单元格的数据组成的列表
    print(table.row_values(i, start_colx=0, end_colx=None))
    # 返回该⾏的有效单元格⻓度，即这⼀⾏有多少个数据
    print(table.row_len(i))
    print("---------------------------")
