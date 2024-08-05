import xlsxwriter

# 创建Excel
workbook = xlsxwriter.Workbook('新建.xlsx')
# 创建工作表
worksheet = workbook.add_worksheet('Sheet1')
# ⾃定义样式，加粗
bold = workbook.add_format({'bold': True})
headings = ['Number', 'testA', 'testB']
data = [
    ['2017-9-1', '2017-9-2', '2017-9-3',
     '2017-9-4', '2017-9-5', '2017-9-6'],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30]
]
worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

# 创建图表对象
chart_col = workbook.add_chart({'type': 'column'})
# 配置第⼀个系列数据
chart_col.add_series({
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values': '=Sheet1!$B$2:$B$7',
    'line': {'color': 'red'}
})
# 配置第⼆个系列数据
chart_col.add_series({
    'name': '=Sheet1!$C$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values': '=Sheet1!$C$2:$C$7',
    'line': {'color': 'yellow'}
})
chart_col.set_title({'name': '折线图'})
chart_col.set_x_axis({'name': 'x轴说明'})
chart_col.set_y_axis({'name': 'y轴说明'})
# 设置样式风格
chart_col.set_style(1)
# 把图表插⼊到worksheet并设置偏移
worksheet.insert_chart('E1', chart_col, {'x_offset': 25, 'y_offset': 10})
workbook.close()
