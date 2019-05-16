#! /usr/bin/python
#coding:utf-8

# 图像、子图、坐标轴和记号
# 到目前为止，我们都用隐式的方法来绘制图像和坐标轴。
# 快速绘图中，这是很方便的。我们也可以显式地控制图像、
# 子图、坐标轴。Matplotlib 中的「图像」指的是用户界面看到的整个窗口内容。在图像里面有所谓「子图」。
# 子图的位置是由坐标网格确定的，而「坐标轴」却不受此限制，
# 可以放在图像的任意位置。我们已经隐式地使用过图像和子图：
# 当我们调用 plot 函数的时候，matplotlib 调用 gca() 函数以及 gcf() 函数来获取当前的坐标轴和图像；
# 如果无法获取图像，则会调用 figure() 函数来创建一个——严格地说，是用 subplot(1,1,1) 创建一个只有一个子图的图像。

# 图像
# 所谓「图像」就是 GUI 里以「Figure #」为标题的那些窗口。
# 图像编号从 1 开始，与 MATLAB 的风格一致，而于 Python 从 0 开始编号的风格不同。以下参数是图像的属性：
# 参数	默认值	描述
# num	1	图像的数量
# figsize	figure.figsize	图像的长和宽（英寸）
# dpi	figure.dpi	分辨率（点/英寸）
# facecolor	figure.facecolor	绘图区域的背景颜色
# edgecolor	figure.edgecolor	绘图区域边缘的颜色
# frameon	True	是否绘制图像边缘
# 这些默认值可以在源文件中指明。不过除了图像数量这个参数，其余的参数都很少修改。
# 你在图形界面中可以按下右上角的 X 来关闭窗口（OS X 系统是左上角）。Matplotlib 也提供了名为 close 的函数来关闭这个窗口。
# close 函数的具体行为取决于你提供的参数：
# 不传递参数：关闭当前窗口；
# 传递窗口编号或窗口实例（instance）作为参数：关闭指定的窗口；
# all：关闭所有窗口。
# 和其他对象一样，你可以使用 setp 或者是 set_something 这样的方法来设置图像的属性。

# 子图
# 你可以用子图来将图样（plot）放在均匀的坐标网格中。
# 用 subplot 函数的时候，你需要指明网格的行列数量，以及你希望将图样放在哪一个网格区域中。
# 此外，gridspec 的功能更强大，你也可以选择它来实现这个功能。

from pylab import *

subplot(2,1,1)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,1,1)',ha='center',va='center',size=24,alpha=.5)

subplot(2,1,2)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,1,2)',ha='center',va='center',size=24,alpha=.5)

# plt.savefig('../figures/subplot-horizontal.png', dpi=64)
show()

# 坐标轴
# 坐标轴和子图功能类似，不过它可以放在图像的任意位置。因此，如果你希望在一副图中绘制一个小图，就可以用这个功能。
axes([0.1,0.1,.8,.8])
xticks([]), yticks([])
text(0.6,0.6, 'axes([0.1,0.1,.8,.8])',ha='center',va='center',size=20,alpha=.5)

axes([0.2,0.2,.3,.3])
xticks([]), yticks([])
text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)

# plt.savefig("../figures/axes.png",dpi=64)
show()

axes([0.1,0.1,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)

axes([0.2,0.2,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.2,0.2,.5,.5])',ha='left',va='center',size=16,alpha=.5)

axes([0.3,0.3,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.3,0.3,.5,.5])',ha='left',va='center',size=16,alpha=.5)

axes([0.4,0.4,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.4,0.4,.5,.5])',ha='left',va='center',size=16,alpha=.5)

# plt.savefig("../figures/axes-2.png",dpi=64)
show()