import pandas as pd
person = {
 "name": ['dylib', 'lucky', 'lucky', 'glen'],
 "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df)
