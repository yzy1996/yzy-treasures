# 核方法

> 相关链接 [SVM]()

为什么要引入核这个概念呢？

举一个二维线性不可分的例子



几个概念需要先明确

- 内积 $<x \cdot y>$
- 



计算相似度

所以一般是 

## 核函数

> Kernel Function



常见的核函数有：

- 线性：$K(\mathbf{x}_1, \mathbf{x}_2) = <\mathbf{x}_1, \mathbf{x}_2>$
- 多项式：$K(\mathbf{x}_1, \mathbf{x}_2) = (\gamma<\mathbf{x}_1, \mathbf{x}_2>+c)^n$
- RBF(Radial basis function)：$K(\mathbf{x}_1, \mathbf{x}_2) = \exp(-\gamma\|\mathbf{x}_1 - \mathbf{x}_2\|^2)$
- Sigmoid：$K(\mathbf{x}_1, \mathbf{x}_2) = \tanh(\gamma<\mathbf{x}_1, \mathbf{x}_2>+c)$



## 核技巧 

> Kernel Trick

首先定义二维空间中的两个点：
$$
\mathbf{x}_1 = (x_{11}, x_{12}) \\
\mathbf{x}_2 = (x_{21}, x_{22})
$$
从二维到三维的映射记作 $\phi$，则有：
$$
\phi(\mathbf{x}_1) = (x_{11}^2, \sqrt{2} x_{11} x_{12}, x_{12}^2) \\
\phi(\mathbf{x}_1) = (x_{21}^2, \sqrt{2} x_{21} x_{22}, x_{22}^2)
$$
用内积计算这两个点的相似度：
$$
<\phi(\mathbf{x}_1), \phi(\mathbf{x}_2)> = x_{11}^2 x_{21}^2 + 2 x_{11}x_{12}x_{21}x_{22} + x_{12}^2 x_{22}^2 \tag{1}
$$
因为这样计算的代价太大了，所以定义一个核函数：
$$
\begin{align}
K(\mathbf{x}_1, \mathbf{x}_2) 
& = <\phi(\mathbf{x}_1), \phi(\mathbf{x}_2)> \\
&= (x_{11}x_{21} + x_{12}x_{22})^2 \\
&= (<\mathbf{x}_1, \mathbf{x}_2>)^2 \\
\end{align} \tag{2}
$$
所以核函数就是直接定义了二维空间中的内积运算，而使用核函数简化计算的技巧就被称为核技巧。







# Reproducing Kernel Hilbert Space

https://zhuanlan.zhihu.com/p/29527729

https://cloud.tencent.com/developer/article/1547677
