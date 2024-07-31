from openpyxl import load_workbook
wb = load_workbook('lucky.xlsx')
ws = wb.active
# print(list(ws.rows))
# 逐行rows输出
"""
for row in ws.rows:
    for cell in row:
        print(cell.value)
"""
# 逐列columns输出
for col in ws.columns:
    for cell in col:
        print(cell.value)
