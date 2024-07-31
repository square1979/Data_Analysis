import xlrd
from xlutils.copy import copy

# 打开文件
workbook = xlrd.open_workbook('test.xls')
# 复制文件
new_workbook = copy(workbook)
# 获取表格数据
sheet = workbook.sheet_by_index(0)
# 获取第一列的值
col = sheet.col_values(0)
cel_val = sheet.cell_value(0, 0)
# print(cel_val)
# 写入表格信息
sheet_write = new_workbook.get_sheet(0)
sheet_write.write(0, 1, "追加内容")
new_workbook.save('test1.xls')
