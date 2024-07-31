import xlrd
file = "test.xlsx"

data = xlrd.open_workbook(file)
# 获取所有sheet
sheets = data.sheets()
print(sheets)
# 获取第一个sheet
sheet = data.sheets()[0]
print(sheet)
# 获取指定序号的sheet
table = data.sheet_by_index(0)
print(table)
# 获取指定名字的sheet
table1 = data.sheet_by_name('Sheet1')
print(table1)
# 返回book中所有⼯作表的名字，以列表返回
names = data.sheet_names()
table2 = data.sheet_by_name(names[0])
print(names)
print(table2)
# 检查某个sheet是否导⼊完毕,返回布尔值
bool1 = data.sheet_loaded("Sheet1")
print(bool1)
