#! /usr/bin/python
#coding:utf-8

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, 7, np.nan, 8, 9])
#print(s)

dates = pd.date_range('20190530', periods=6)
#print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A' : 1,
                                'B':pd.Timestamp('20190530'),
                                'C':pd.Series(1, index=list(range(4)), dtype='float32'),
                                'D':np.array([3]*4, dtype='int32'),
                                'E':pd.Categorical(['test', 'train', 'test', 'train']),
                                'F':'foo'})
#print(df2)

print(df.head())
print(df.tail(3))
print(df.index)

print(df.describe())

sort = df.sort_index(axis=1, ascending=False)
print(sort)

sort = df.sort_values(by='B')
print(sort)

print(df['A'])

print(df[0:3])

loc = df.loc[dates[0]]
print(loc)

loc = df.loc[:, ['A', 'B']]
print(loc)

loc = df.loc['20190530':'20190531', ['A', 'B']]
print(loc)

loc = df.loc['20190530', ['A', 'B']]
print(loc)

loc = df.loc[dates[0], 'A']
print(loc)

print("~~~~~~~~~~~~~~~")
at = df.at[dates[0], 'A']
print(at)

iloc = df.iloc[3]
print(iloc)