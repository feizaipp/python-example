#! /usr/bin/python
#coding:utf-8

import numpy as np
# import matplotlib.pyplot as plt
from pylab import *

figure(figsize=(10,6), dpi=80)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 改变线条的颜色和粗细
# 首先，我们以蓝色和红色分别表示余弦和正弦函数，而后将线条变粗一点。接下来，我们在水平方向拉伸一下整个图。
plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plot(X, S, color="red",  linewidth=2.5, linestyle="-")

# 设置图片边界
plt.xlim(-4.0,4.0)
plt.xticks(np.linspace(-4,4,9,endpoint=True))

plt.ylim(-1.0,1.0)
plt.yticks(np.linspace(-1,1,5,endpoint=True))

show()
