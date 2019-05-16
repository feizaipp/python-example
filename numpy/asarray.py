#! /usr/bin/python
#coding:utf-8

import numpy as np

x = [1,2,3]
a = np.asarray(x)
print(a)

x = (1,2,3)
a = np.asarray(x)
print(a)

x = [(1,2,3), (4,5)]
a = np.asarray(x)
print(x)
print(a)

s = b'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)

'''
# python 2.x
s = 'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)
'''

ls = range(5)
it = iter(ls)

x = np.fromiter(it, dtype=float)
print(x)

# 从数值范围创建数组
x = np.arange(5)
print(x)

x = np.arange(10,20,2)
print(x)

# 等差数列
x = np.linspace(1,10,10)
print(x)

x = np.linspace(1,10,5)
print(x)

a = np.linspace(1,1,10)
print(a)

# 将 endpoint 设为 false ， 不包含终止值
a = np.linspace(10,20,5, endpoint=False)
print(a)

# 设置间距
a = np.linspace(1,10,10,retstep=True)
print(a)

b = np.linspace(1,10,10).reshape(10,1)
print(b)

# 创建等比数列
a = np.logspace(1.0, 2.0, num=10)
print(a)

a = np.logspace(0,9,10,base=2)
print(a)