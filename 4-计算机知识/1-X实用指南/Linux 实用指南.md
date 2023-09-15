# Linux 使用指南

[toc]

## apt

Advanced Package Tool (apt)，是一款适用于Unix和Linux系统的应用程序管理器。能帮助处理依赖项。

apt-get 最早于1998年发布，apt 最早于2014年发布。目前应该优先使用 apt.



常用命令

```
apt install 
apt remove 
apt purge
apt upgrade

sudo apt list
sudo apt remove -y <package name>
sudo apt clean && sudo apt autoremove
```





## Linux 系统相关

查看linux 内核

```bash
uname -a 
```

文件储存含义



可执行文件默认放在 `/usr/local/bin` ；
库文件默认放在 `/usr/local/lib` ；
配置文件默认放在 `/usr/local/etc` ；
其它的资源文件放在 `/usr /local/share` 



## Linux 环境变量PATH

cuda 是软连接


ls -al

查看  ls -l /usr/local | grep cuda 

经过测试，local 下的多个文件夹 输出的 nvcc 版本是一样的



添加软连接 symlinked symbolic link

```
ln -s libcuda.so.1.1 libcuda.so.1
ln -s libcuda.so.1.1 libcuda.so
sudo ln -s /usr/lib/wsl/lib/libcuda.so.1 /usr/local/cuda/lib64/libcuda.so
```





profile 是对所有用户有效

bashrc 是对当前用户有效

查看PATH

```bash
echo $PATH
```

> 是用`:`进行分割的

`export`命令能直接修改`PATH`的值

```bash
export PATH=$PATH:/usr/local/cuda-11.2/bin

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.2/lib64:/usr/lib/x86_64-linux-gnu
```

> 立即生效，但只对当前终端有效

如果想要永久有效，就得去编辑`bashrc`文件了

```bash
nano ~/.bashrc

# 在最后一行加上
export PATH=$PATH:/usr/local/cuda/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64

打开新的终端或者 
source ~/.bashrc 生效
```

打开新的终端或者 `source ~/.bashrc`





Command 'nvcc' not found, but can be installed with:



## 文件或文件夹操作

a 是指这个文件，a/ 是指 a 这个文件夹，所以移动的时候需要注意

还有一个是移动文件夹下的文件，所有文件是 a/*



### 删除

```bash
# 删除文件
rm filename1 filename2

# 删除某一后缀文件
rm *.pdf

# 强制删除文件
rm -f filename

# 删除文件夹
rm -r dirname

# 删除空文件夹
rm -d dirname

# 强制删除文件夹
rm -rf dirname
```

### 移动

``` shell
# 移动文件夹
mv [-fiv] source destination

# -f 强制直接移动而不询问
# -i 若目标文件已存在，会询问是否覆盖
# -u 若目标文件已存在，且源文件比较新，才会更新

将/test1 目录下的 file1 移动到 test3 目录，并重命名为 file2，可以使用
mv /test1/file1 /test3/file2

注意：如果是把一个文件移动到一个目录，需要先创建这个目录，不然会将这个文件，重命名为那个目录
```

### 复制

```bash
cp xx xx
```

### 重命名

```
同 mv 
```



### 查看

```bash
# 查看文件大小
ls -l xx

# 查看文件夹大小
du -sh

# 查看文件夹内文件数量(包含子目录)
ls -lR | grep "^-" | wc -l

# 查看文件夹内文件数量(不包含包含子目录)
ls -l | grep "^-" | wc -l

# 查看文件夹数量
ls -l | grep "^d" | wc -l
```

### 压缩

> 对不同压缩格式的用法也不同

安装 

```bash
##　针对zip格式

# 压缩
zip -q -r html.zip /home/html

zip -q -r html.zip * 当前目录下所有文件打包

# 解压
unzip 

# 不想要打印输出的话，加-q

##　针对gz格式, all you need is
tar -zxvf
```



## 修改文件权限

`.sh`文件，既可以通过`./xx.sh`执行，也可以通过`bash xx.sh`执行，但前者有时候需要添加权限。

通过`ls`显示的颜色可以区分，绿色的为可执行文件

```bash
# 变为可执行文件
chmod +x filename

# 变为不可可执行文件
chmod -x filename
```



## 文件头

bash文件的开头通常有这一句，是什么意思呢

```bash
#!/bin/bash
```

同理，

```bash
#!/usr/bin/env python与#!/usr/bin/python的区别
```



## SCP传文件

```bash
# 从本地传到服务器
scp test.txt zhiyuyang4@htgc2t.cs.cityu.edu.hk:~/

# 从服务器传到本地
scp zhiyuyang4@htgc2t.cs.cityu.edu.hk:~/test.txt ./

# SCP传文件夹
scp -r test zhiyuyang4@htgc2t.cs.cityu.edu.hk:~/
scp -r zhiyuyang4@htgc2t.cs.cityu.edu.hk:~/test ./
```





## wget下载

使用 curl 或者 wget



`wget -O <filename> <link>`



使用 `wget -c xx` 断点下载文件

或者使用 `gdown xx` 下载谷歌文件











## 激活和关闭图形界面

sudo service lightdm start

sudo /etc/init.d/lightdm stop



Ubuntu 的 ctrl + alt + F1-7





## 如果没有root权限

https://github.com/0x00009b/pkget 用这个可以

https://unix.stackexchange.com/questions/42567/how-to-install-program-locally-without-sudo-privileges



## tmux 终端

**终端多路复用器：ssh + tmux**

> 简述流程和问题：使用ssh登录服务器，就建立了一个 **session** (会话)，这个session会打开并绑定一个terminal (终端)，一般我们就在这个terminal 里运行程序看打印输出 (进程)。
>
> 现在问题来了，如果ssh网络断开或者你关掉了这个session -> 会导致这个terminal 关掉，进程终止 (就像你执行了 `ctrl + c` 一样)。
>
> 但我们的训练不能停啊，希望无论什么原因断开连接后，程序依然能运行。

最推荐 `tmux` ，它干了一件什么事呢？简单讲 (不一定对) ：在<u>会话</u><u>终端</u>执行 `tmux` 后，创建了一个新的“副终端”，而这个副终端不会随着<u>会话</u>的中断而被杀掉，之后可以随时再切换到这个副终端。所以我们只需要在这个副终端里执行我们的程序就好了。

具体用法是：

1. 先安装，检查安装没用 `tmux --version` 

2. 启动

   ```bash
   % 默认启动方式，多个副终端的编号是0，1...
   tmux
   
   % 如果想自定义名称
   tmux new -s <name>
   ```

3. 退出副终端

   先按 `ctrl+b` ，全松开再按 `d`

   或者输入 `tmux detach`

4. 查看现存副终端列表

   ```bash
   tmux ls
   ```

5. 恢复副终端

   ```bash
   % 0是副终端编号，也可以是你设的名称
   tmux attach -t 0
   ```

6. 副终端里切换其他副终端

   ```bash
   % 0是副终端编号，也可以是你设的名称
   tmux switch -t 0
   ```

7. 杀死副终端

   ```bash
   % 0是副终端编号，也可以是你设的名称
   tmux kill-session -t 0
   ```
   
8. 拆分屏幕

   ```bash
   tmux split-window
   ```



不能滚动屏幕 ctrl + b : setw -g mouse on

就可以了

但还不能复制



解决复制问题：mac 下按住 option 选择








## tensorboard 本地浏览器访问远程服务器

- 操作步骤：
  - 本地终端运行`ssh -L local_port:remote_ip:remote_port user@server_ip` 创建 ssh 连接终端
  - 在打开的远程终端运行 tb `tensorboard --logdir xxx --port remote_port (--ip 127.0.0.1)`
  - 在本地浏览器访问：`http://127.0.0.1:local_port`
- e.g. 
  - `ssh -L 16006:127.0.0.1:6006 user@1.2.3.4`
  - `tensorboard --logdir ./logs --port 6006`
  - 本地浏览器访问 `http://127.0.0.1:16006`
    **使用MobaTextEditor会导致编码不是utf-8 Unicode**

> 问题描述：使用MobaXterm来访问服务器是很方便的一种选择，同时它也提供对文本文件的可视化编辑(双击文件会用MobaTextEditor打开)。但编辑后保存格式通过 `file xx` 可见---由UTF-8 Unicode 变成了 Non-ISO extended-ASCII，进而导致读文件时对中文的编码报错。

解决办法：1. 使用nano命令行编辑文本 2. 右键文件使用默认编译器(vscode)打开编辑







## Vim 使用

```shell
vim <filename>
```

进去之后是处于命令模式，无法修改文件

按`:`后可以输入一些保存，退出的指令



```shell
:q # 退出不保存
:x # 退出并保存
dd # 删除光标所在行
```





按 `i` 进入编辑模式





按 `esc` 退出编辑模式 并 进入命令模式







## grep 搜索

```shell
grep test *file # 查找后缀有 file 字样的文件中包含 test 字符串的文件
```











dpkg -l | grep Fortran

export FC=gfortran-4.8





 GNU Compiler Collection (gcc)

includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages





## make build

### 2、如果指定 `--prefix`

比如： `--prefix=/usr/local/keepalived` ，则此软件的所有文件都放到 `/usr/local/keepalived` 目录下，很整齐。

### 3、其他优点：

- 卸载软件时，只须简单的删除该安装目录，就可以把软件卸载得干干净净；
- 移植软件时，只需拷贝整个目录到另外一个机器即可；

当然要卸载程序，也可以在原来的make目录下用一次make uninstall，但前提是make文件指定过uninstall 。





## 编译器

编译器

CC 是 C compile

CXX C++

FC Fortran 77



软链接



```bash
export CC=/mnt/cache/yangzhiyuan/miniconda3/envs/nr3d/bin/x86_64-conda-linux-gnu-gcc
```

