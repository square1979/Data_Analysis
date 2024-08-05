import pandas as pd

df = pd.read_csv('test.csv')
# head()
# head( *n* ) ⽅法⽤于读取前⾯的 n ⾏，如果不填参数 n ，默认返回 5 ⾏。
print(df.head())
"""
Name Team Number
Position Age Height Weight
College Salary
0 Avery Bradley Boston Celtics 0.0
PG 25.0 6-2 180.0 Texas
7730337.0
1 Jae Crowder Boston Celtics 99.0
SF 25.0 6-6 235.0 Marquette
6796117.0
2 John Holland Boston Celtics 30.0
SG 27.0 6-5 205.0 Boston University
 NaN
3 R.J. Hunter Boston Celtics 28.0
SG 22.0 6-5 185.0 Georgia State
1148640.0
4 Jonas Jerebko Boston Celtics 8.0
PF 29.0 6-10 231.0 NaN
5000000.0
"""

# tail()
# tail( *n* ) ⽅法⽤于读取尾部的 n ⾏，如果不填参数 n ，默认返回 5 ⾏，空⾏各个字段的值返回 NaN。
print(df.tail())
"""
Name Team Number Position
 Age Height Weight College Salary
453 Shelvin Mack Utah Jazz 8.0 PG
26.0 6-3 203.0 Butler 2433333.0
454 Raul Neto Utah Jazz 25.0 PG
24.0 6-1 179.0 NaN 900000.0
455 Tibor Pleiss Utah Jazz 21.0 C
26.0 7-3 256.0 NaN 2900000.0
456 Jeff Withey Utah Jazz 24.0 C
26.0 7-0 231.0 Kansas 947276.0
457 NaN NaN NaN NaN
 NaN NaN NaN NaN NaN
"""
print(df.tail(10))
"""
Name Team Number
Position Age Height Weight College
Salary
448 Gordon Hayward Utah Jazz 20.0
SF 26.0 6-8 226.0 Butler 15409570.0
449 Rodney Hood Utah Jazz 5.0
SG 23.0 6-8 206.0 Duke 1348440.0
450 Joe Ingles Utah Jazz 2.0
SF 28.0 6-8 226.0 NaN 2050000.0
451 Chris Johnson Utah Jazz 23.0
SF 26.0 6-6 206.0 Dayton 981348.0
452 Trey Lyles Utah Jazz 41.0
PF 20.0 6-10 234.0 Kentucky 2239800.0
453 Shelvin Mack Utah Jazz 8.0
PG 26.0 6-3 203.0 Butler 2433333.0
454 Raul Neto Utah Jazz 25.0
PG 24.0 6-1 179.0 NaN 900000.0
455 Tibor Pleiss Utah Jazz 21.0
C 26.0 7-3 256.0 NaN 2900000.0
456 Jeff Withey Utah Jazz 24.0
C 26.0 7-0 231.0 Kansas 947276.0
457 NaN NaN NaN
NaN NaN NaN NaN NaN
NaN
"""

# info() ⽅法返回表格的⼀些基本信息
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 458 entries, 0 to 457 #⾏数，458 ⾏，第⼀⾏编号为 0
Data columns (total 9 columns): #列数，9列
# Column Non-Null Count Dtype #各列的数据类型
"""
print(df.info())
# non-null 为⾮空数据，我们可以看到上⾯的信息中，总共 458⾏，College 字段的空值最多。
