import xlwt

# 创建workbook并设置编码
workbook = xlwt.Workbook(encoding='ascii')

# 创建新的sheet表
worksheet = workbook.add_sheet('new_sheet1')

# 写入内容
worksheet.write(0, 0, '帅气的')
worksheet.write(1, 0, '气的')
worksheet.write(2, 0, '的')

# 保存文件
workbook.save('new_sheet1.xls')
