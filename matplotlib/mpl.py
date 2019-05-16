#! /usr/bin/python
#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

# 介绍
# Matplotlib 可能是 Python 2D-绘图领域使用最广泛的套件。
# 它能让使用者很轻松地将数据图形化，并且提供多样化的输出格式。
# 这里将会探索 matplotlib 的常见用法。

# IPython 以及 pylab 模式
# IPython 是 Python 的一个增强版本。它在下列方面有所增强：
# 命名输入输出、使用系统命令（shell commands）、排错（debug）能力。
# 我们在命令行终端给 IPython 加上参数 -pylab （0.12 以后的版本是 --pylab）之后，
# 就可以像 Matlab 或者 Mathematica 那样以交互的方式绘图。

# pylab
# pylab 是 matplotlib 面向对象绘图库的一个接口。
# 它的语法和 Matlab 十分相近。也就是说，它主要的绘图命令和 Matlab 对应的命令有相似的参数。

# 初级绘制
# 这一节中，我们将从简到繁：先尝试用默认配置在同一张图上绘制正弦和余弦函数图像，然后逐步美化它。
# 第一步，是取得正弦函数和余弦函数的值：

# X 是一个 numpy 数组，包含了从 −π 到 +π 等间隔的 256 个值。
# C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组。

# Matplotlib 的默认配置都允许用户自定义。你可以调整大多数的默认配置：
# 图片大小和分辨率（dpi）、线宽、颜色、风格、坐标轴、坐标轴以及网格的属性、
# 文字与字体属性等。不过，matplotlib 的默认配置在大多数情况下已经做得足够好，
# 你可能只在很少的情况下才会想更改这些默认配置。

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c,s = np.cos(X), np.sin(X)

plt.plot(X, c)
plt.plot(X, s)

plt.show()

# 默认配置的具体内容
# 下面的代码中，我们展现了 matplotlib 的默认配置并辅以注释说明，
# 这部分配置包含了有关绘图样式的所有配置。代码中的配置与默认配置完全相同，你可以在交互模式中修改其中的值来观察效果。
# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
from pylab import *

# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.0, linestyle="-")

# 设置横轴的上下限
xlim(-4.0,4.0)

# 设置横轴记号
xticks(np.linspace(-4,4,9,endpoint=True))

# 设置纵轴的上下限
ylim(-1.0,1.0)

# 设置纵轴记号
yticks(np.linspace(-1,1,5,endpoint=True))

# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
show()
