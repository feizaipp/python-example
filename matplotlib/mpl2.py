#! /usr/bin/python
#coding:utf-8

import numpy as np
# import matplotlib.pyplot as plt
from pylab import *

figure(figsize=(10,6), dpi=80)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plot(X, S, color="red",  linewidth=2.5, linestyle="-")

# 设置记号的
# plt.xlim(X.min()*1.1, X.max()*1.1)
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

# plt.ylim(C.min()*1.1,C.max()*1.1)
# plt.yticks([-1, 0, +1])

# 设置记号的标签
plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(C.min()*1.1,C.max()*1.1)
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

show()
