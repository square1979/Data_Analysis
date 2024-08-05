import xlsxwriter
import datetime

# 创建新的工作簿
workbook = xlsxwriter.Workbook('新建.xlsx')
# 创建新的工作表 = new_sheet
worksheet = workbook.add_worksheet('new_sheet')
# 写入数据
worksheet.write('A1', '你想吃什么？')
worksheet.write(1, 0, '我想吃炒饭')
# 写入数字以及函数
worksheet.write(2, 2, 301314)
worksheet.write(3, 2, 301314)
worksheet.write(4, 2, '=SUM(C3:C4)')
# 写入图片
worksheet.insert_image(0, 5, '迪丽热巴.png')
# 将图片设置为链接
worksheet.insert_image(10, 5, '迪丽热巴.png', {'url': 'https://www.baidu.com/'})
# 写入日期
d = workbook.add_format({'num_format': 'yyyy-mm-dd'})
worksheet.write(0, 2, datetime.datetime.strptime('2024-02-15', '%Y-%m-%d'), d)

# 设置样式
f = workbook.add_format({'border': 1, 'font_size': 44,
                         'bold': True, 'align': 'center',
                         'border_color': '#99CCFF', 'bg_color': '99FFFF'})
""" 
字体颜⾊：color 字体加粗：bold 字体⼤⼩：font_size ⽇期格式：num_format 超链接：url
下划线设置：underline 单元格颜⾊：bg_color 边框：border 对⻬⽅式：align 
"""
worksheet.write('A5', 'lucky', f)
# 设置第一行的行高
worksheet.set_row(0, 100, f)
# 设置第一列的列宽
worksheet.set_column('A:B', 40, f)
# 批量向单元格输入数据
worksheet.write_column('A15', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
worksheet.write_row('B12', [90, 70, 60, 50, 40, 30, 20])
# 合并单元格写⼊
worksheet.merge_range(7, 5, 11, 8, 'merge_range')
# 保存文件
workbook.close()
