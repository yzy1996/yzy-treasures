## matplotlib库的使用



今天介绍一个mpl_toolkits库的使用，它可以用来绘制三维视图



最基本的使用方法如下：

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.show()
```



fig.add_subplot(111, projection='3d') 



plt.gca(*projection*='3d')



效果是一模一样的，都是创建了一个三维实例



plt.figure()的说明

可写可不写，不写在使用的时候会自动为你创建

写可以在括号内为图命名，默认是figure1



隐藏 Matplotlib 图中的空白和边框

保存图片

```python
fig=plt.imshow(img)
plt.axis('off')
plt.savefig('image.png', bbox_inches='tight',pad_inches = 0)

plt.imsave("kapal.png",img)
```



## 颜色

cmp 

https://xkcd.com/color/rgb/

https://matplotlib.org/stable/gallery/color/named_colors.html

https://yoksel.github.io/handy-colors/#full-palette



C1 这样的是指的Tableau Color，数字代表第几个，例如C1就是 tab:orange



markers 可以更加丰富

https://matplotlib.org/stable/tutorials/text/mathtext.html





坐标轴的设置：



```python
ax.set_xlabel(r'$x_1$', size = 20, labelpad = 8.5)

labelpad：类型为浮点数，默认值为None，即标签与坐标轴的距离。
```



