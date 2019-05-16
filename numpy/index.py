#! /usr/bin/python
#coding:utf-8

import numpy as np

# 以下实例获取数组中(0,0)，(1,1)和(2,0)位置处的元素。
x = np.array([[1,  2],  [3,  4],  [5,  6]])
print(x.shape)
y = x[[0,1,2],  [0,1,0]]
print(y)

# 以下实例获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print (x)
rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print (y)
print(rows)
print(cols)

print('~~~~~~~~~~~~~~~')
a = np.array([[1,2,3], [4,5,6],[7,8,9]])
b = a[1:3, 1:3]
print(b)
c = a[1:3,[1,2]]
print(c)
d = a[...,1:]
print(d)

# 我们可以通过一个布尔数组来索引目标数组。
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print(x[x>5])

#以下实例使用了 ~（取补运算符）来过滤 NaN。
a = np.array([np.nan,  1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])
print(~np.isnan(a))

# 以下实例演示如何从数组中过滤掉非复数元素。
a = np.array([1,  2+6j,  5,  3.5+5j])
print (a[np.iscomplex(a)])

# 花式索引指的是利用整数数组进行索引。
# 花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。
# 对于使用一维整型数组作为索引，如果目标是一维数组，
# 那么索引的结果就是对应位置的元素；如果目标是二维数组，那么就是对应下标的行。
x=np.arange(32).reshape((8,4))
print(x)
print (x[[4,2,1,7]])

print('~~~~~~~~~~')
x=np.arange(32).reshape((2,4,4))
print(x)
print('~~~~~~~~')
print (x[[1,1]])

# 传入多个索引数组（要使用np.ix_）
x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])