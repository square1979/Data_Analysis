import xlwt

# 创建工作簿
workbook = xlwt.Workbook(encoding='ascii')
# 创建工作表
worksheet = workbook.add_sheet('new_sheet1')
# 创建样式对象
style = xlwt.XFStyle()
# 设置样式
font = xlwt.Font()
# 设置字体
font.name = "微软雅黑"
# 设置字体加粗
font.bold = True
# 设置斜体
font.italic = True
# 设置下划线
font.underline = True
# 设置样式给style
style.font = font
# 向单元格写入内容
worksheet.write(0, 0, '行文')
worksheet.write(1, 0, "聪明的", style)
worksheet.write(2, 0, "努力的", style)

workbook.save('new_sheet3.xls')
