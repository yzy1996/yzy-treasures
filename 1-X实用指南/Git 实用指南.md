# Git用法

参考学习：https://git-scm.com/book/zh/v2



## 身份认证

最新的Github认证体系不再接受用户名和密码了，需要一个personal access token

推荐先[安装 gh 工具](https://cli.github.com/)，这样可以很方便进行网页授权

```shell
conda install gh --channel conda-forge

gh auth login

# 很简单的几个选择后，最后选择login with web
# 是可以点击链接跳转网页，然后输入授权码
# 这样会在本地的.gitconfig里写入你的登陆授权

gh auth setup-git
```



## 添加ssh密钥

使用submodule 必须要这个，为了使用ssh建立连接，需要在本地电脑拿到一个密钥然后授权给[github](https://github.com/settings/keys/new)

```shell
ssh-keygen -t rsa -C "<your email>"

# 回车回车..

cat id_rsa.pub 
# 或者用文本编辑器打开 id_rsa.pub 这个文件，路径在上一步有显示 (~/.ssh/id_rsa.pub)

# 复制粘贴到 https://github.com/settings/ssh/new 的key区域 (下图)，title随意

# 👌

1. vim ~/.ssh/id_rsa.pub
2. copy the ssh key
3. Go to the github settings
4. Select the option ssh keys
5. Remove the old ssh keys not used anymore.
6. Add a new ssh key.
7. Try running the "git submodule update --recursive"
```

<img src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220427163340248.png" alt="image-20220427163340248" style="zoom:33%;" />













## 第一步clone仓库

打开github你想要的仓库网页，会提供直接的clone链接，复制粘贴到下面即可。

```bash
# public repo
git clone <xx.git>

# private repo
git clone <xx.git>

# include submodules
git clone --recurse-submodules <xx.git>

# 后续
git submodule update --init --recursive
```



git submodule sync

git submodule update --init --recursive

git submodule update --remote



## 维护这个仓库

下拉网络上的最新版本

上传本地上的版本

添加子模块



有了一个仓之后，就可以下拉云端的最新代码，以及上传本地的最新代码

```
git fetch

git merge
```



discard本地修改文件

```
git checkout
```



提交修改

```
git commit 
```



只更新某一个文件

```
git config core.sparsecheckout true

echo 你要的文件名 >> .git/info/sparse-checkout
git pull origin master

```





因为本地你也会修改一些东西，且希望保持不变，



```
git stash
git pull 
git stash pop
```





```
git diff 
```



子模块

```
git submodule add
```





```python
git status
```



### stash 暂存修改

> 本地修改和pull冲突时，可以先暂存本地修改，pull下来后再恢复本地修改

```bash
# 如果要对所有修改一键隐藏
git stash

# 如果只想隐藏某些文件
git stash push <file1> <file2>

# 如果需要一部分隐藏，一部分提交，可以一个一个选择
git stash -p 
# 然后 y 就是stash, n 就是 commit

# 恢复
git stash pop
```









删除仓库历史

1. 完全重建版本库

```bash
# 切换到latest_branch分支下
git checkout --orphan latest_branch
# 添加所有文件
git add -A
# 提交更改
git commit -am "清除所有历史版本以减少仓库大小，请重新从远程拷贝此仓库"
# 删除分支
git branch -D master
# 将当前分支重命名
git branch -m master
# 最后，强制更新存储库
git push -f origin master
```

2. 创建一个新分支，然后删除旧分支

   ```bash
   git checkout 
   ```

   



## 减少小修改

> 对很小的修改，连续多次commit，会让log看上去很复杂，而一般即使是小版本更新也不是改一下就提交一下的。自己一个人看就没什么，而如果是多人协作，还是在别人还未pull的时候，撤销一下push，然后再重新commit+push

其实就是撤销提交，有两种分别是：

```python
git reset --hard
git reset --soft
```

他们的区别在于，前者是直接回退到前一个版本，这次提交的修改直接被冲掉；而后者只是撤回了commit，修改内容还在。所以一般情况下应该使用 `soft`



而对应到 Github Desktop 上就是 `History` 里的 `Revert change in commit`，然后再到 Change 里点一下 `undo`。





查看版本记录

git reflog main



放弃本地分支内容，直接拉取远程内容

git reset --hard origin/master



git add





git pull
git submodule sync
git submodule update --init --recursive





git fast-forward





## 下拉代码仓

如果本地没有任何改动，是可以直接拉的

但如果本地有改动，

- 你的改动和云端冲突
- 你的改动和云端不冲突



如果本地有改动，





需要先设置 git pull 是 mege 模式还是 rebase 模式

https://backlog.com/git-tutorial/cn/stepup/stepup1_4.html

git config pull.rebase false



### 分支的合并

首次使用需要进行一个设置 git config pull.ff true

merge









## 子模块

**添加**

```shell
git submodule add <url> <path>
```



```shell
git submodule add <url> 

git commit

git submodule init
git submodule update
```



每次想要更新的时候

```shell
git submodule sync --recursive
git submodule update --init --recursive
```



克隆含有子模块的项目



## 回滚代码

```
git reset --hard HEAD^ 
git push origin
```





## gitignore

它只能忽略那些原来没有被track的文件，因此需要先都改成未track的状态

```bash
git rm -r --cached .

git add .

git commit -m 'update .gitignore'
```

