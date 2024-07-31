import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('sheet1')
# 创建边框对象
border = xlwt.Borders()
border.left = xlwt.Borders.DOUBLE
border.right = xlwt.Borders.DOUBLE
border.top = xlwt.Borders.DOUBLE
border.bottom = xlwt.Borders.DOUBLE

# 设置四边颜色
border.left_colour = 0  # 黑
border.right_colour = 1  # 白
border.top_colour = 2  # 红
border.bottom_colour = 3  # 酸橙色

style = xlwt.XFStyle()
style.borders = border

# 写入内容进行保存
worksheet.write(0, 0, "行文", style)
workbook.save('test1.xls')
