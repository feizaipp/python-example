#! /usr/bin/python
#coding:utf-8

import numpy as np

a = np.arange(24)

print(a)
print(a.ndim)

b = a.reshape(2,4,3)
print(b)
print(b.ndim)

print(b.shape)

# ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。

x = np.array([1,2,3,4,5], dtype = np.int8)
print(x.itemsize)

y = np.array([1,2,3,4,5], dtype = np.float64)
print(y.itemsize)

z = np.array([1,2,3,4,5])
print(z.itemsize)
print(z.flags)