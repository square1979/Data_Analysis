import pandas as pd

# 创建数据
data = {
    'name': ['迪丽热巴', '古力娜扎', 'jack'],
    'age': [1, 2, 3]
}

mydata = pd.DataFrame(data)
print(type(mydata), mydata)
