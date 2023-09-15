

conda官网 https://docs.conda.io/projects/conda/en/latest/

下载安装Anaconda: https://www.anaconda.com/products/distribution#Downloads

下载安装Miniconda：https://docs.conda.io/en/latest/miniconda.html

下载安装Miniforge：https://conda-forge.org/miniforge/

[toc]

# Anaconda vs Miniconda vs Miniforge

他们的核心都是包含**conda**这一工具，来实现 **python** `环境(environment)`和`包(package)`管理的，（其实不仅仅可以用来管理python，很多语言R, Java, C都支持）；然后就可以通过：

- `conda install numpy` 来安装包
- `conda create -n myenv python=3.9` 来创建环境

Anaconda 和 Miniconda 是一个公司的产品，商用是付费的，个人暂时免费；而Miniforge是由社区主导，用GitHub托管，完全免费。Miniconda 和 Miniforge 是差不多的产物，代表着轻量化，而Anaconda是完整版，就略显臃肿。这里先比较 [Anaconda vs Miniconda](#Anaconda-vs-Miniconda)，而后比较 [Miniconda vs Miniforge](#Miniconda-vs-Miniforge)。



## Anaconda vs Miniconda

(老手) **Miniconda** = `Python + conda` (with minimal dependencies, like openssl, ncurses...)

(新手) **Anaconda** = `Python + conda + meta package anaconda` (about 160 Python pkgs, like curl, numpy, pandas...)

> 简言之，Anaconda 多了一些基本的包，很省事，不用再单独安装了，但也有一些可能一直用不到，白白占用了空间。Miniconda 可以按需求安装库，但也可以借助`conda install anaconda` 手动实现anaconda一样的 pre-installed package。一个是安装初期花费更多时间下载，一个是后期花更多时间单独安装。我个人倾向于 Miniconda，一切从简。



## Miniconda vs Miniforge

Miniforge 使用 `conda-forge` 作为默认 channel，而 Miniconda 使用 `anaconda` 作为默认channel。channel的含义在这里介绍一下：

> conda channels (源) 是 packages 存储的位置，也即是你是从哪个来源下载这个包，对应到conda内部处理则是下载文件的链接。因为不同源会有相同名字的包，因此必须指定来源，同时安装conda的时候也会有一个默认的channel。**目前主流的就是 conda-forge**，齐全且更新快。如果有多个channel，他们会按顺序确定优先级，优先的源上找不到，就会到下一个优先级的源上去找。还可以设置channel的优先级是否strict，如果是strict的话，则只会在这一个源上查找。

然后 Miniforge 比 Anaconda\Miniconda 更早支持了Apple M1芯片。2022年5月6日Anaconda官方宣布原生支持了Apple M1版本。在苹果官方的[Tensorflow加速训练教程](https://developer.apple.com/metal/tensorflow-plugin/)中也是推荐的Miniforge。

> 简言之，我个人更倾向于 Miniforge，社区万岁。



# Conda vs Pip

conda package的来源在前面介绍过了，而pip的来源是 PyPI (Python Package Index)。pip是专门针对python打包而成的，属于wheels or source distributions，需要compiler来安装；而conda packages are binaries，因此包含例如C语言写的库，同时也不需要compilers。pip的包是可以自行制作上传的，没有经过验证，而conda源是经过同行验证过的。

通常我们安装一个python包，直接用`pip install <pkg-name>`就行，但如果我们想要多个python环境，也就需要用到virtualenv；同时如果这个包没有不是 Python packages，是用C语言写的；这时候就需要Conda登场了，它同时解决了以上所有问题。

> 简言之，比较推荐的是用conda创建虚拟python环境，然后 `conda install pip` 后使用pip来安装需要的包，遇到不支持pip的，或者特殊编译的，可以根据开发者的说明使用conda进行安装。
>
> 所以优先`pip install`，不行再`conda install`。

需要注意的是 pip 和 conda 安装包对象的名称可能是不一样的，例如 `conda - pytorch`，``pip - torch`。



---

补充：现在还有新的 [Mamba](https://mamba.readthedocs.io/en/latest/index.html) 用来替代 conda，提供更快的速度。使用上用`mamba`替换掉`conda`就行，其他用法完全一致。

补充：Homebrew是mac下的一个软件管理器，跟python无关



# 参考资料

https://stackoverflow.com/questions/45421163/anaconda-vs-miniconda

https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda

https://www.anaconda.com/blog/understanding-conda-and-pip
