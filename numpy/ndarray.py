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

c = a.reshape(3, 2,4,1)
print(c)
print(c.ndim)

print(c.shape)