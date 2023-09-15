# Vscode 使用指南



## 1. 安装

[安装地址](https://code.visualstudio.com/Download)，提供一个 **user installer** (首页默认下载的是这个) 以及一个 **system installer**，本意是为了多用户登录时候，前者只能当前用户使用，后者可以所有用户使用，但我们大多数基本都是单一用户，所以没什么区别，但在安装和使用的时候后者需要管理员权限。**我推荐就安装 user 版本。**

安装有一步是问你是否选择额外设置时，记得全部选上

- 将“通过code 打开“操作添加到windows资源管理器**文件**上下文菜单

  > 右键文件能够多一个 `通过Code打开` 的选项

- 将“通过code 打开”操作添加到windows资源管理器**目录**上下文菜单

  > 右键文件夹能够多一个 `通过Code打开` 的选项

- 将Code注册为受支持的文件类型的编辑器

  > 默认使用 VScode 打开诸如 txt,py 等文本类型的文件

- 添加到PATH（重启后生效）

  > 命令行可以直接 `code .`



## 2. 优化使用

> 美化界面+更顺手的插件推荐

代码颜色主题





## 3. 使用





### 常用快捷键

`alt+z` 长代码自动换行 

### 一些设置

显示隐藏文件  `files.exclude`

`explorer.sortOrder` 修改文件列表排序方式

`Workbench>Editor>Show Tabs`

> 控制打开的编辑器是否显示在选项卡中。双击的才固定，单击打开的是斜体只会显示一个。



Workbench>Editor:Enable Previe



### 调试 Debug

> 带参数调试 arg paser

debug 选择 open launch.json

![image-20220702195007669](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220702195007669.png)

添加 args

```json
"args":["--model", "gan"]
```



```
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Debug",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "SH-IDC1-10-140-0-152",
                "port": 27678
            },
            "variablePresentation": {
                "all": "hide",
                "class": "group",
                "function": "hide",
                "protected": "inline",
            }
        }
    ],
}
```











python 代码的formatting, 我选择 black 

添加额外的一项 --line-length 110
