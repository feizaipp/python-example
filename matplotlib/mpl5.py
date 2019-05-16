
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

# plot(X, C, color="blue", linewidth=2.5, linestyle="-")
# plot(X, S, color="red",  linewidth=2.5, linestyle="-")
# 添加图例
plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")


# 给一些特殊点做注释
# 我们希望在 2π/3 的位置给两条函数曲线加上一个注释。
# 首先，我们在对应的函数图像位置上画一个点；然后，向横轴引一条垂线，以虚线标记；最后，写上标签。
t = 2*np.pi/3
plot([t,t],[0,np.cos(t)],
         color ='blue',  linewidth=1.5, linestyle="--")
scatter([t,],[np.cos(t),], 50, color ='blue')
annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)),  xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plot([t,t],[0,np.sin(t)],
         color ='red',  linewidth=1.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='red')
annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)),  xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
legend(loc='upper left', frameon=False)
show()
