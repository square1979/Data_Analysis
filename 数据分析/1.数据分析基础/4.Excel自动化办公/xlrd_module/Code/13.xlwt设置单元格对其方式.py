import xlwt

"""
    VERT_CENTER = 0x01 居中对⻬(垂直⽅向上)
    VERT_BOTTOM = 0x02 低端对⻬
    HORZ_LEFT = 0x01 左端对⻬
    HORZ_CENTER = 0x02 居中对⻬(⽔平⽅向上)
    HORZ_RIGHT = 0x03 右端对⻬
"""

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('Sheet1')
worksheet.write(1, 1, '行为段落')
# 设置单元格对其方式
style = xlwt.XFStyle()
al = xlwt.Alignment()
al.horz = 0x02  # 水平居中
al.vert = 0x01  # 居中对齐
style.alignment = al

# 写入另一个值对比
worksheet.col(2).width = 20*256
worksheet.write(2, 2, '年少老程', style)
workbook.save('test3.xls')
