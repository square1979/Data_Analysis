import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet1')
# 合并行列
worksheet.write_merge(1, 2, 0, 2, '帅气的行文')
worksheet.write_merge(6, 7, 4, 5, '行文')

# 保存
workbook.save('test1.xls')
