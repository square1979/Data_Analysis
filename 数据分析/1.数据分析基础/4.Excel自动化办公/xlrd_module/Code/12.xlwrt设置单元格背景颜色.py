import xlwt

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('Sheet1')
# 创建样式
pattern = xlwt.Pattern()
# 设置背景模式
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# 设置背景颜色
pattern.pattern_fore_colour = 52

style = xlwt.XFStyle()
style.pattern = pattern

# 写入内容并设置样式
worksheet.write(1, 1, '你真帅', style)
workbook.save('test2.xls')
