#! /usr/bin/python
#coding:utf-8

import numpy as np

# 以下函数用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作。 它们基于 Python 内置库中的标准字符串函数。
# 这些函数在字符数组类（numpy.char）中定义。

# 函数	描述
# add()	对两个数组的逐个字符串元素进行连接
print ('连接两个字符串：')
print (np.char.add(['hello'],[' xyz']))
print ('\n')
 
print ('连接示例：')
print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))
# multiply()	返回按元素多重连接后的字符串
print (np.char.multiply('Runoob ',3))
# center()	居中字符串
'''
np.char.center(str , width,fillchar) ：
str: 字符串，width: 长度，fillchar: 填充字符
'''
print (np.char.center('Runoob', 20,fillchar = '*'))
# capitalize()	将字符串第一个字母转换为大写
print (np.char.capitalize('runoob'))
# title()	将字符串的每个单词的第一个字母转换为大写
print (np.char.title('i like runoob'))
# lower()	数组元素转换为小写
#操作数组
print (np.char.lower(['RUNOOB','GOOGLE']))
 
# 操作字符串
print (np.char.lower('RUNOOB'))
# upper()	数组元素转换为大写
#操作数组
print (np.char.upper(['runoob','google']))
 
# 操作字符串
print (np.char.upper('runoob'))
# split()	指定分隔符对字符串进行分割，并返回数组列表
# 分隔符默认为空格
print (np.char.split ('i like runoob?'))
# 分隔符为 .
print (np.char.split ('www.runoob.com', sep = '.'))
# splitlines()	返回元素中的行列表，以换行符分割
# 换行符 \n
print (np.char.splitlines('i\nlike runoob?')) 
print (np.char.splitlines('i\rlike runoob?'))
# strip()	移除元素开头或者结尾处的特定字符
# 移除字符串头尾的 a 字符
print (np.char.strip('ashok arunooba','a'))
# 移除数组元素头尾的 a 字符
print (np.char.strip(['arunooba','admin','java'],'a'))
# join()	通过指定分隔符来连接数组中的元素
# 操作字符串
print (np.char.join(':','runoob'))
# 指定多个分隔符操作数组元素
print (np.char.join([':','-'],['runoob','google']))
# replace()	使用新字符串替换字符串中的所有子字符串
print (np.char.replace ('i like runoob', 'oo', 'cc'))
# decode()	数组元素依次调用str.decode
a = np.char.encode('runoob', 'cp500') 
print (a)
print (np.char.decode(a,'cp500'))
# encode()	数组元素依次调用str.encode
a = np.char.encode('runoob', 'cp500') 
print (a)
