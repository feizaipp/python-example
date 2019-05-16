#! /usr/bin/python
#coding:utf-8

import numpy as np

# 使用标量类型
dt = np.dtype(np.int32)
print(dt)

# int8, int 16, int32 int 64 可以用'i1' 'i2' 'i3' 'i4'字符串替代
dt = np.dtype("i4")
print(dt)

# 字节顺序标注
dt = np.dtype("<i4")
print(dt)

# 创建结构化数据类型
dt = np.dtype([('age', np.int8)])
print(dt)
# 将数据结构类型应用于 ndarray 对象
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)

#类型子段名可以用于存取实际的 age 列
print(a['age'])

# 创建结构化数据类型
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)

print(a)
