#! /usr/bin/python
#coding:utf-8

import numpy as np

a = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
choices = [-10, 10]
b = np.choose(a, choices)
print(b)

c = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index = np.array([0,2,1,0])
d = np.choose(index,c.T)
print(d)

y_hat = np.array([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
y = np.array([0, 2], dtype='int32')
e = np.choose(y, y_hat.T)
print(e)

