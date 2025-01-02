# Linux 使用指南

> 记录自己最常用的一些操作！


## 一. 开始 - Login

第一个最常用的当然是访问服务器，比如我最喜欢的就是用编辑器vscode，关于[vscode的使用指南]()我也写过一篇。第一次只需要在远程资源管理器里添加里添加 ssh username@ip 然后敲入密码就可以了；但**免密码登录**相信你肯定是不会拒绝的。

1. 本地windows/mac创建ssh密钥，注意-执行完下面的指令后，提示的步骤都按回车跳过即可。

   ```shell
   ssh-keygen
   ```

   生成的密钥对，会存储在`~/.ssh/id_rsa` 和 `~/.ssh/id_rsa.pub` 文件中。

2. 本地命令行上传密钥。

   ```shell
   ssh-copy-id <username>@<remote-server>
   ```

3. 输完一次密码后，以后就再也不用输了。

连接上服务器后，再资源管理器里选择打开一个文件夹路径，就可以开心Coding啦！！

如果想重新生成密钥对，可以使用`-R`选项，可以清楚 `known_hosts` 文件中的旧条目。

```shell
ssh-keygen -R <hostname_or_ip>
```



## 二. 文件或文件夹操作

> filename 是指这个文件，filename/ 是指 filename 这个文件夹，所以移动的时候需要注意。还有一个是移动文件夹下的文件，所有文件是 filename/*。

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

> 对不同压缩格式的用法也不同，记得先要安装

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

### 修改文件权限

`.sh`文件，既可以通过`./xx.sh`执行，也可以通过`bash xx.sh`执行，但前者有时候需要添加权限。

通过`ls`显示的颜色可以区分，绿色的为可执行文件，或者直接看权限 `ls -l`

```bash
# 变为可执行文件
chmod +x filename

# 变为不可可执行文件
chmod -x filename
```

### SCP传文件

```bash
# 从本地传到服务器
scp test.txt zhiyuyang4@htgc2t.cs.cityu.edu.hk:~/

# 从服务器传到本地
scp zhiyuyang4@htgc2t.cs.cityu.edu.hk:~/test.txt ./

# SCP传文件夹
scp -r test zhiyuyang4@htgc2t.cs.cityu.edu.hk:~/
scp -r zhiyuyang4@htgc2t.cs.cityu.edu.hk:~/test ./
```

## 三. tmux 终端

因为终端是和你登录绑定的，连接断开，终端也会被杀掉，因此为了避免程序意外被终端，使用tmux是一个选择.

这个东西原理叫**终端多路复用器：ssh + tmux**

> 简述流程和问题：使用ssh登录服务器，就建立了一个 **session** (会话)，这个session会打开并绑定一个terminal (终端)，一般我们就在这个terminal 里运行程序看打印输出 (进程)。
>
> 现在问题来了，如果ssh网络断开或者你关掉了这个session -> 会导致这个terminal 关掉，进程终止 (就像你执行了 `ctrl + c` 一样)。
>
> 但我们的训练不能停啊，希望无论什么原因断开连接后，程序依然能运行。

最推荐 `tmux` ，它干了一件什么事呢？简单讲 (不一定对) ：在<u>会话</u><u>终端</u>执行 `tmux` 后，创建了一个新的“副终端”，而这个副终端不会随着<u>会话</u>的中断而被杀掉，之后可以随时再切换到这个副终端。所以我们只需要在这个副终端里执行我们的程序就好了。

具体用法是：

1. 先安装，检查安装没有 `tmux --version` 

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

> 冒号是需要的

就可以了但还不能复制解决复制问题：mac 下按住 option 选择，windows 按住 shift 再选择



## 三. 下载和安装

### 下载

下载我们使用 curl 或者 wget

`wget -O <filename> <link>`

使用 `wget -c xx` 断点下载文件

或者使用 `gdown xx` 下载谷歌文件

### 安装

Advanced Package Tool (apt)，是一款适用于Unix和Linux系统的应用程序管理器。能帮助处理依赖项。apt-get 最早于1998年发布，apt 最早于2014年发布。目前应该优先使用 apt。

**常用命令**

```shell
apt install 
apt remove 
apt purge
apt upgrade

sudo apt list
sudo apt remove -y <package name>
sudo apt clean && sudo apt autoremove
```



## 四. 用命令行编辑文件

一般使用的是vim和nano两种，我自己更习惯用nano.

### vim

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

### nano

```shell
nano <filename>
```

最下面一行会提示你一些相关的操作。



## 五. 搜索 grep

全称是 **global regular expression**。

有时候我们需要搜索一些文件,或者历史指令

```shell
grep test *file # 查找后缀有 file 字样的文件中包含 test 字符串的文件
```



## 六. 关于进程 PID

PID 是进程标志符的意思， `ps` 命令是

```shell
ps -u <user>  # 查看用户的进程
```

根据名称匹配进程

```shell
pgrep <name>  # 查找指定名称的进程
```



终止进程呢？使用`kill`

```shell
kill PID
```

