import xlrd
from xlutils.copy import copy

# 打开Excel
workbook = xlrd.open_workbook('test.xls')
# 复制文件到新的文件
new_workbook = copy(workbook)
# 保存文件
new_workbook.save('test1.xls')
