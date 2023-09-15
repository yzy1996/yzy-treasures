

shell 的类型有很多，mac,linux默认都是bash




> bash 和 zsh (z shell) 都是 mac 终端自带的 shell 命令解释器，两者都兼容所有命令和操作，但 zsh 更好一些，macos目前默认也是 zsh。zsh 读取的配置文件是 `~/.zshrc `文件



Oh My ZSH 是一个主题管理工具

```shell
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

配置文件为 `~/.zshrc`

其中 `ZSH_THEME` 可以修改主题，还可以设置为 random ，默认是 robbyrussell

### 安装插件

- 代码高亮插件zsh-syntax-highlighting：`git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting`
- 历史命令智能提示插件zsh-autosuggestions：`git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions`  按右方向键
- z：快速访问目录，自带直接添加。
- web-search：终端中直接进行网页搜索，自带。
- extract：压缩直接用x就可以完成，自带。
- wd：对目录进行映射，自带。
- sudo：按两下ESC在命令开头增加sudo命令，自带。
- encode64：Base64 编码，自带。
- urltools：url编码工具,有urlencode和urldecode，自带。
  

下载好插件，在~/.zshrc文件中把插件添加进去：

plugins=(
    git
    z
    web-search
    zsh-autosuggestions
    zsh-syntax-highlighting
)





修改主题





配置conda 



找到这个文件`~/.bash_profile`

复制里面内容

粘贴到 `~/.zshrc` 末尾



z 是一个文件夹快捷跳转插件，对于曾经跳转过的目录，只需要输入最终目标文件夹名称，就可以快速跳转，避免再输入长串路径，提高切换文件夹的效率。效果如下：





zsh 支持为较长命令设置一个别名，这样在使用时可以快捷输入。

这里以 cd ~/projects/alicode/blog 这个命令来举例：

在 .zshrc 中键入：

alias cdblog="cd ~/projects/alicode/blog"
