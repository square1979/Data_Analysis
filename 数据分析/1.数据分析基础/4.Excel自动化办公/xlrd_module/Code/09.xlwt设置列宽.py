"""
xlwt中列宽的值表示⽅法：默认字体0的1/256为衡量单位。
xlwt创建时使⽤的默认宽度为2960，既11个字符0的宽度
所以我们在设置列宽时可以⽤如下⽅法：width = 256 * 20 256为衡量单位，20表示20个字符宽度
"""
import xlwt

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('new_sheet1')

worksheet.write(0, 0, '行文')
worksheet.write(0, 2, '牛马')

# 设置列宽
worksheet.col(0).width = 256 * 20
worksheet.col(2).width = 256 * 10

workbook.save('new_sheet4.xls')
