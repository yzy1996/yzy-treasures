相关链接，[一文解释conda,pip,anaconda,miniconda,miniforge](./一文解释conda,pip,anaconda,miniconda,miniforge.md) | [conda-cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)



这里主要展示 conda 的使用



# 安装conda

```shell
# 安装 miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh


# 安装 miniforge 
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
```



### 升级

```bash
conda update -n base conda
conda update conda
```



### 卸载

参考：https://github.com/conda-forge/miniforge





## 有关channel

> channels (源) 是 packages 存储的位置，也即是你是从哪个来源下载这个包，对应到conda内部处理则是下载文件的链接。因为不同源会有相同名字的包，因此必须指定来源，同时安装conda的时候也会有一个默认的channel。目前主流的就是 conda-forge，齐全且更新快。如果有多个channel，他们会按顺序确定优先级，优先的源上找不到，就会到下一个优先级的源上去找。还可以设置channel的优先级是否strict，如果是strict的话，则只会在这一个源上查找。

channel的设置文件为 `.condarc`，

```shell
# 查看 .condarc 文件内容，是以key+value的样式
conda config --get

# 如果只想看channel
conda config --get channels

# 查看 所有设置
conda config --show


# 添加新channel到最 高 优先级
conda config --add channels new_channel

# 与上面等价
conda config --prepend channels <new_channel>

# 添加新channel到最 低 优先级
conda config --append channels <new_channel>

# 删除
conda config --remove channels conda-forge

conda config --set channel_priority strict

conda config --set channel_priority false
```

默认的channel指的是repo.anaconda.com

https://repo.anaconda.com/pkgs/main

- 可以在每次使用的时候指定新的channel (如果指定多个将按优先顺序搜索)，例如 `conda install scipy --channel conda-forge`。

- 也可以修改默认channel，这样不指定也是优先在设置的channle



```bash
conda config --add channels conda-forge
conda config --remove channels conda-forge
```





## 关于环境 env

```shell
# 查看已有环境
conda env list
conda info --envs

# 1. 创建（肯定）带名字的
conda create -n <name> python=3.10

# 2. 创建（可选）带地址的
conda create -p /cpfs2/user/yangzhiyuan/envs/test python=3.9

# 删除
conda remove -n py36 --all

# 导出环境
conda env export > environment.yml

# 从environment.yml文件创建
conda env create -f environment.yml
```



## 关于包 pkg

直接去查对应包官方给出的安装命令吧！

如果遇到 Solving environment: failed with initial frozen solve. Retrying with flexible solve. 说明你要的某些包冲突了。

```shell
conda install <...>

# conda -c 是 

# 查看历史版本
conda list --revisions

# 重制环境版本
conda install --revision REV_NUM

# 升级所有包
conda update --all

# 清理垃圾
conda clean -a
```



有时候你会看到带有`-c`的命令，代指的是 `--channel CHANNEL` 。它决定了你的包是从组织下载的

```shell
# 查看当前默认channel
conda config --show
```



> Additional channel to search for packages. 





疑难解答

the environment is inconsistent, please check the package plan carefully







```shell
conda init --reverse --dry-run
conda init --reverse

CONDA_BASE_ENVIRONMENT=$(conda info --base)
echo The next command will delete all files in ${CONDA_BASE_ENVIRONMENT}
rm -rf ${CONDA_BASE_ENVIRONMENT}

echo ${HOME}/.condarc will be removed if it exists
rm -f "${HOME}/.condarc"
```



