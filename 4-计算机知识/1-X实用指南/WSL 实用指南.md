# 教你使用 WSL



## 1. 安装 WSL

这里参照官方[最新教程](https://learn.microsoft.com/en-us/windows/wsl/install)，默认你满足环境要求，以下记录核心步骤。

- 用管理员权限打开PowerShell，输入：

```powershell
wsl --install
```

- 重启电脑后就安装好了，默认安装的是Ubuntu
- 输入用户名和密码设置

[设置 WSL 开发环境](https://learn.microsoft.com/zh-cn/windows/wsl/setup/environment?source=recommendations)

##  2. 使用 WSL 

- 更新常规包

  ```bash
  sudo apt update && sudo apt upgrade
  ```

- 基础指令

  ```bash
  wsl --list --verbose
  wsl -t <name>
  ```



sudo apt install gcc g++



其他可以参考 [Linux 使用指南](./Linux 使用指南)

## 配置 GPU 支持

参考资料 https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2





关闭

wsl --shutdown
