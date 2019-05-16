#! /usr/bin/python
#coding:utf-8

import numpy as np
# import matplotlib.pyplot as plt
from pylab import *

figure(figsize=(10,6), dpi=80)

ax = subplot(111)
# 移动脊柱
# 坐标轴线和上面的记号连在一起就形成了脊柱
# （Spines，一条线段上有一系列的凸起，是不是很像脊柱骨啊~），
# 它记录了数据区域的范围。它们可以放在任意位置，不过至今为止，我们都把它放在图的四边。
# 实际上每幅图有四条脊柱（上下左右），为了将脊柱放在图的中间，
# 我们必须将其中的两条（上和右）设置为无色，然后调整剩下的两条到合适的位置——数据空间的 0 点。
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plot(X, S, color="red",  linewidth=2.5, linestyle="-")

show()
