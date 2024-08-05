"""
Pandas 数据清洗
数据清洗是对⼀些没有⽤的数据进⾏处理的过程。
很多数据集存在数据缺失、数据格式错误、错误数据或重复数据的情况，
如果要对使数据分析更加准确，就需要对这些没有
⽤的数据进⾏处理。在这个教程中，我们将利⽤ Pandas包来进⾏数据清洗。
"""
import pandas as pd

df = pd.read_csv('property-data.csv')
print(df['NUM_BEDROOMS'])
# 判断该列数据单元格是否为空
print(df['NUM_BEDROOMS'].isnull())
