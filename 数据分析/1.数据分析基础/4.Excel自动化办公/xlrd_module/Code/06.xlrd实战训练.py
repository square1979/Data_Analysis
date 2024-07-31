import xlrd

xlsx = xlrd.open_workbook('test.xlsx')
# 通过sheet名查找：xlsx.sheet_by_name("sheet1")
# 通过索引查找：xlsx.sheet_by_index(3)
table = xlsx.sheet_by_index(1)

# 获取单个表格值 (1,0)表示获取第2⾏第1列单元格的值
value = table.cell_value(1, 0)
print("第2⾏1列值为", value)

# 获取表格⾏数
nrows = table.nrows
print("表格⼀共有", nrows, "⾏")

# 获取第1列所有值(列表⽣成式)
name_list = [str(table.cell_value(i, 0)) for i in range(0, nrows)]
print("第1列所有的值：", name_list)
print("---------------")
# 不用列表⽣成式
name = []
for i in range(0, nrows):
    name_list = str(table.cell_value(i, 0))
    name.append(name_list)
print("第1列所有的值：", name)
