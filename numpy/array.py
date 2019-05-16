#! /usr/bin/python
#coding:utf-8

import numpy as np

# 修改数组形状
# 函数	描述
# reshape	不改变数据的条件下修改形状
# flat	数组元素迭代器
# flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
# ravel	返回展开数组

# numpy.reshape
# numpy.reshape 函数可以在不改变数据的条件下修改形状，
# 格式如下： numpy.reshape(arr, newshape, order='C')
# arr：要修改形状的数组
# newshape：整数或者整数数组，新的形状应当兼容原有形状
# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。
a = np.arange(8)
print ('原始数组：')
print (a)
print ('\n')
 
b = a.reshape(4,2)
print ('修改后的数组：')
print (b)

# numpy.ndarray.flat
# numpy.ndarray.flat 是一个数组元素迭代器，实例如下:
a = np.arange(9).reshape(3,3) 
print ('原始数组：')
for row in a:
    print (row)
#对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print ('迭代后的数组：')
for element in a.flat:
    print (element)

# numpy.ndarray.flatten
# numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
a = np.arange(8).reshape(2,4)
print ('原数组：')
print (a)
print ('\n')
# 默认按行
 
print ('展开的数组：')
print (a.flatten())
print ('\n')
 
print ('以 F 风格顺序展开的数组：')
print (a.flatten(order = 'F'))

# numpy.ravel
# numpy.ravel() 展平的数组元素，顺序通常是"C风格"，
# 返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。
# 该函数接收两个参数：numpy.ravel(a, order='C')
# 参数说明：
# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 ravel 函数之后：')
print (a.ravel())
print ('\n')
 
print ('以 F 风格顺序调用 ravel 函数之后：')
print (a.ravel(order = 'F'))

# 翻转数组
# 函数	描述
# transpose	对换数组的维度
# ndarray.T	和 self.transpose() 相同
# rollaxis	向后滚动指定的轴
# swapaxes	对换数组的两个轴

# numpy.transpose
# numpy.transpose 函数用于对换数组的维度，格式如下：
# numpy.transpose(arr, axes)
# 参数说明:
# arr：要操作的数组
# axes：整数列表，对应维度，通常所有维度都会对换。
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a )
print ('\n')
 
print ('对换数组：')
print (np.transpose(a))

# numpy.ndarray.T 类似 numpy.transpose：
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)

# numpy.rollaxis
# numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：
# numpy.rollaxis(arr, axis, start)
# 参数说明：
# arr：数组
# axis：要向后滚动的轴，其它轴的相对位置不会改变
# start：默认为零，表示完整的滚动。会滚动到特定位置。
a = np.arange(8).reshape(2,2,2)
print ('原数组：')
print (a)
print ('\n')
# 将轴 2 滚动到轴 0（宽度到深度）
 
print ('调用 rollaxis 函数：')
print (np.rollaxis(a,2))
# 将轴 0 滚动到轴 1：（宽度到高度）
print ('\n')
 
print ('调用 rollaxis 函数：')
print (np.rollaxis(a,2,1))

# 多维数组轴的概念, axis 表示的是维数， index=0 表示最外层的数组比较
print("~~~~~~~~~~~~~~~~~~~")
a = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
print(a)
print(a.shape)
print(a.max(axis=0))
print('\n')
print(a.max(axis=1))
print('\n')
print(a.max(axis=2))

# numpy.swapaxes
# numpy.swapaxes 函数用于交换数组的两个轴，格式如下：
# numpy.swapaxes(arr, axis1, axis2)
# arr：输入的数组
# axis1：对应第一个轴的整数
# axis2：对应第二个轴的整数
print('~~~~~~~~~~~~~~')
a = np.arange(8).reshape(2,2,2)
print ('原数组：')
print (a)
print ('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
 
print ('调用 swapaxes 函数后的数组：')
print (np.swapaxes(a, 2, 0))