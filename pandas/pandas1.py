#! /usr/bin/python
#coding:utf-8

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, 7, np.nan, 8, 9])
#print(s)

dates = pd.date_range('20190530', periods=6)
#print(dates)

# 创建 DataFrame 
#                            A               B               C             D
# 2019-05-30  0.234434 -0.858556  0.692620  0.055391
# 2019-05-31  1.639617  1.461722  0.639001 -0.744521
# 2019-06-01  0.266079 -0.508822 -0.021935 -0.748942
# 2019-06-02  0.080890 -0.374334 -0.369761 -0.561226
# 2019-06-03 -0.021484 -0.952084  0.236083  0.966010
# 2019-06-04 -0.434366 -0.924862 -0.549927 -0.842728
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A' : 1,
                                'B':pd.Timestamp('20190530'),
                                'C':pd.Series(1, index=list(range(4)), dtype='float32'),
                                'D':np.array([3]*4, dtype='int32'),
                                'E':pd.Categorical(['test', 'train', 'test', 'train']),
                                'F':'foo'})
#print(df2)

# 显示前5行
#print(df.head())

# 显示最后3行
#print(df.tail(3))

# 显示行索引名称
#print(df.index)

# 显示汇总信息
#              A         B         C         D
#count  6.000000  6.000000  6.000000  6.000000
#mean   0.435600  0.583733  0.702193  0.458471
#std    0.848937  0.874122  1.255279  0.769842
#min   -0.839268 -0.565863 -1.147483 -0.630145
#25%   -0.052765 -0.093352  0.057117  0.088379
#50%    0.622387  0.755903  0.703912  0.336271
#75%    0.887855  1.175966  1.521585  1.020288
#max    1.509567  1.616903  2.317157  1.454387
#print(df.describe())

# 按轴1的递减顺序排列
sort = df.sort_index(axis=1, ascending=False)
#print(sort)

# 按列头为B，从小到大排序
sort = df.sort_values(by='B')
#print(sort)

# 获得列头为A的列
#print(df['A'])

# 获得前三行
#print(df[0:3])

# 根据列索引获得当前行的数据
loc = df.loc[dates[0]]
#print(loc)

# 获得列头为 A和B 的两列
loc = df.loc[:, ['A', 'B']]
#print(loc)

# 获得20190530 到 20190531，两个列索引的列头为 A和B 的数据
loc = df.loc['20190530':'20190531', ['A', 'B']]
#print(loc)

# 获得20190530列索引的 列头为 A和B 的数据
loc = df.loc['20190530', ['A', 'B']]
#print(loc)

# 获得列索引0的，列头为A的数据
loc = df.loc[dates[0], 'A']
#print(loc)

#print("~~~~~~~~~~~~~~~")
# 获得列索引0的，列头为A的数据
at = df.at[dates[0], 'A']
#print(at)

# 获得第三行的数据
iloc = df.iloc[3]
#print(iloc)

# 获取轴1取[3,5)行和轴2取[0,2)列
iloc = df.iloc[3:5, 0:2]
#print(iloc)

# 获取轴1取1、2、4行和轴2取0、2列
iloc = df.iloc[[1, 2, 4], [0, 2]]
# print(iloc)

# 获取第1到第3行
iloc = df.iloc[1:3, :]
print(iloc)