import xlwt

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('new_sheet1')
worksheet.write(0, 0, '帅气的')
worksheet.write(2, 1, '魔法盾')

# 设置行高
style = xlwt.easyxf('font: height 720;')
# 选定设置样式的行
row = worksheet.row(0)
# 添加样式
row.set_style(style)
workbook.save('new_sheet1.xls')
