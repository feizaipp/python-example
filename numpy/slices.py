#! /usr/bin/python
#coding:utf-8

import numpy as np

a = np.arange(10)
s = slice(2,7,2)
print(a[s])

a = np.arange(10)
b = a[2:7:2]
print(b)

# 冒号 ':' 的解释：如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素。
# 如果为 [2:]，表示从该索引开始以后的所有项都将被提取。
# 如果使用了两个参数，如 [2:7]，那么则提取两个索引(不包括停止索引)之间的项。
a = np.arange(10)
print(a[2])
print(a[2:])
print(a[2:5])

# 多维数组同样适用上述索引提取方法：
a = np.arange(9).reshape(3,3)
print(a)
print('从数组索引 a[1:] 处开始切割')
print(a[1:])

print('~~~~~~~~~~')
# 切片还可以包括省略号 ...，来使选择元组的长度与数组的维度相同。
# 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素
