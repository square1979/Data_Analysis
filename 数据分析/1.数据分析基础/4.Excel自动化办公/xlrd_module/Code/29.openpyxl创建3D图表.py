from openpyxl import Workbook
from openpyxl.chart import Reference, BarChart3D

# 新建工作簿
wb = Workbook()
# 激活工作表功能
ws = wb.active
# 创建数据
rows = [('None', 2021, 2022),
        ('平板', 2, 4),
        ('手机', 20, 40),
        ('笔记本', 40, 80)]
# 将数据写入工作表
for row in rows:
    ws.append(row)
# 创建3d图表对象
chart = BarChart3D()
# 设置图表名称
chart.title = '3D图表'
# 添加数据
data = Reference(ws, min_col=2, max_col=3, min_row=1, max_row=4)
# 添加标签
labels = Reference(ws, min_col=1, min_row=2, max_row=4)
# 添加数据到3D对象
chart.add_data(data, titles_from_data=True)
# 设置类别轴额标签
chart.set_categories(labels)
chart.x_axis.delete = False
chart.y_axis.delete = False
# 图表放置位置
ws.add_chart(chart, 'E5')
# 保存文件
wb.save('图表3D.xlsx')
