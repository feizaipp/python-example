#! /usr/bin/python
#coding:utf-8

import numpy as np

x = np.empty([3,2], dtype=int)
print(x)

y = np.zeros(5)
print(y)

z = np.zeros((5,), dtype = int)
print(z)

m = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(m)
print(m['x'])

x = np.ones(5)
print(5)

y = np.ones([2,2], dtype = int)
print(y)