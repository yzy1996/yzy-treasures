# <p align=center>Cityu_HPC 实用指南 </p>



参考资料：[User Guide CityU](https://www.cityu.edu.hk/csc/deptweb/support/guidelines/studentlan/HPC_userguide.htm) ｜ [slurm 命令大全](https://slurm.schedmd.com/pdfs/summary.pdf) ｜[上交超算平台用户手册](https://docs.hpc.sjtu.edu.cn/job/slurm.html)



## 1. 介绍

本集群采用的是Slurm管理系统（不懂的看开头学习资料），由登陆节点提交任务按需分配计算节点。

| 账号身份 | 最大GPU数量 | 最大节点数 | 最大使用时长 |
| :------: | :---------: | :--------: | :----------: |
| student  |      2      |     1      |     1天      |
|  staff   |      4      |     2      |     3天      |

关于存储空间，默认的Home Directory: 50GB fixed; Scratch Directory: 300GB by default。

目前可用的计算节点有：gpu_7d1g [002-004， 009-013] 共8*8块 32G V100



## 2. 使用

首先安装Miniconda的环境

```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```



### 2.1 数据

只有登陆节点是联网的，所以下载只能在登陆节点完成



### 2.2 查看空闲资源

```shell
sinfo -N --p gpu_7d1g
```

State 的状态有 `drain(节点故障)，alloc(节点在用)，idle(节点可用)，down(节点下线)，mix(节点部分占用，但仍有剩余资源）`。



### 2.3 开始训练

尝试下来不支持srun模式，每次只让申请一块GPU



**2.3.1 交互式**

```shell
salloc -p gpu_7d1g --gres=gpu:1
```

执行后会分配资源

![image-20230405111859447](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/202304051119403.png)

同时终端ip会从 `[zhiyuyang4@hpclogin02 ~]$` 的目录变成了`[zhiyuyang4@hpc-gpu003 ~]$`，这里就可以执行 `nvidia-smi` 查看 GPU了。



```shell
# 直接运行
python xx.py
```



2.3.2 sbatch提交

…待整理



### 2.4 查看任务

```shell
squeue -u zhiyuyang4
```



### 2.5 取消任务

```shell
# 通过上一步获取 id
scancel JOBID
```

取消后会自动跳转回登陆节点



## mess

```shell
srun --partition=gpu_7d1g --qos=normal  --nodes=1 --cpus-per-task=4 --ntasks-per-node=1 
--gres=gpu:1  --mem=50G -t1:00:0 --pty bash -i 
```

using A100

```shell
salloc -A pa_cs_department -p special_cs --gres=gpu:a100:4
```

using V100

```shell
salloc -p gpu_7d1g --gres=gpu:1 -n 4 --cpus-per-task=6 
```

```shell
squeue -u zhiyuyang4 -o "%C"
```

```shell
sinfo -o "%c" 查看节点核心数
sinfo -n hpc-gpu003 
```

