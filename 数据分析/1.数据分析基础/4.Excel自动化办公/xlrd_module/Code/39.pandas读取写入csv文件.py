import pandas as pd

# 读取csv文件
data = pd.read_csv('黄河.CSV', encoding='GBK')
# to_string() ⽤于返回 DataFrame 类型的数据，
# 如果不使⽤该函数，则输出结果为数据的前⾯ 5 ⾏和末尾 5 ⾏，中间部分以... 代替。
print(data.to_string())
# ⽤ to_csv() ⽅法将 DataFrame 存储为 csv ⽂件：
data.to_csv('site.csv')
# 注意： 在写⼊csv⽂件会默认将索引写⼊ 如果不需要索引 则需添加参数进⾏处理
