import xlsxwriter

# 创建Excel
workbook = xlsxwriter.Workbook('新建.xlsx')
# 创建工作表
worksheet = workbook.add_worksheet('Sheet1')
# ⾃定义样式，加粗
bold = workbook.add_format({'bold': True})
data = [
 ['closed', 'active', 'reopen', 'NT'],
 [1012, 109, 123, 131]
]
# 写⼊数据
worksheet.write_row('A1', data[0], bold)
worksheet.write_row('A2', data[1])

# 创建图表对象
chart_col = workbook.add_chart({'type': 'pie'})
# 配置第⼀个系列数据
chart_col.add_series({
    'name': 'Bug Analysis',
    'categories': '=Sheet1!$A$1:$D$1',
    'values': '=Sheet1!$A$2:$D$2',
    'points': [
        {'fill': {'color': '#00CD00'}},
        {'fill': {'color': 'red'}},
        {'fill': {'color': 'yellow'}},
        {'fill': {'color': 'gray'}}
    ]
})

chart_col.set_title({'name': 'Bug Analysis'})
# 设置样式风格
chart_col.set_style(1)
# 把图表插⼊到worksheet并设置偏移
worksheet.insert_chart('E1', chart_col, {'x_offset': 25, 'y_offset': 10})
workbook.close()
