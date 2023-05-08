#  <p align=center>Cityu HTC 实用指南 </p> 

[toc]

## 登录ip

```shell
# CPU, 128G Memory
gateway.cs.cityu.edu.hk

# htgc1, Ubuntu20.04, V100-16G, CUDA11.2
htgc1.cs.cityu.edu.hk
htgc1t.cs.cityu.edu.hk

# htgc2, 2080Ti
htgc2.cs.cityu.edu.hk
htgc2t.cs.cityu.edu.hk

# V100
htgc3.cs.cityu.edu.hk
htgc3t.cs.cityu.edu.hk
```

`ssh zhiyuyang4@remote_ip`



配置sshkey login

```shell
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server
```

注意上述操作`ssh-copy-id`不支持windows

```
$USER_AT_HOST="zhiyuan@10.20.96.27:8088"
$PUBKEYPATH="$HOME\.ssh\id_rsa.pub"

Get-Content "$PUBKEYPATH" | Out-String | ssh $USER_AT_HOST "powershell `"New-Item -Force -ItemType Directory -Path `"`$HOME\.ssh`"; Add-Content -Force -Path `"`$HOME\.ssh\authorized_keys`" `""
```







GPU  CUDA 在 /usr/local

```
export CUDA_HOME=/usr/local/cuda
export PATH=/$PATH:usr/local/cuda/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
```



## 代码｜数据

- 根目录 ~ 是 `/home/grads/zhiyuyang4` 

- 代码存在 `~/code/` 有100G上限
- 数据存在`/public/zhiyuyang4/data` 有200G上限



推荐推荐使用 OneDrive | Google Drive 作为文件中继。不用Git的原因是不支持大文件，一些log会超过100M。

如果要用 Google Drive的话，利用工具 [gdrive](https://github.com/prasmussen/gdrive) 。

```bash
# 安装步骤
wget https://github.com/prasmussen/gdrive/releases/download/2.1.1/gdrive_2.1.1_linux_386.tar.gz
tar -xvf gdrive_2.1.1_linux_386.tar.gz
./gdrive about
```



使用步骤

> 只推荐用来同步文件内容的更新，数量更新到服务器端去改变，**云端的文件增删是无效的**

```bash
# 1. 创建一个同步文件夹
gdrive mkdir <foldername>

# 2. 会返回一个 file_id，复制他

# 3. 同步文件，同时也声明了哪些文件是需要同步的
gdrive sync upload <your_file> <file_id>

# 如果是服务器上修改代码了，就还是 upload
gdrive sync upload <your_file> <file_id>
gdrive sync upload ./code 1VlCSz_mPs_GbHrBNF3wL9nATI3hvwBWZ

# 如果是本地修改代码了(注意只能修改已有文件，如果要新建文件，需要先在服务器端新建了然后上传，因为需要一个同步的flag；同时避免增删文件，)，就是 download
gdrive sync download <file_id> <your_file>
gdrive sync download 1VlCSz_mPs_GbHrBNF3wL9nATI3hvwBWZ ./code

# 删除文件
gdrive sync content 1VlCSz_mPs_GbHrBNF3wL9nATI3hvwBWZ
gdrive delete 1VlCSz_mPs_GbHrBNF3wL9nATI3hvwBWZ
```



当下使用

```bash
gdrive list
gdrive sync list
gdrive sync content 1-QMtr3LzVf0bQYTxV5ddsE7bcqaBlfjM

1-QMtr3LzVf0bQYTxV5ddsE7bcqaBlfjM # projected_gan-main
gdrive sync upload ./code/projected_gan-main 1-QMtr3LzVf0bQYTxV5ddsE7bcqaBlfjM
gdrive sync download 1-QMtr3LzVf0bQYTxV5ddsE7bcqaBlfjM ./code/projected_gan-main

1-Pv6xsVhcskQW1FwcnO-KORytBM53gID # neuralgen
gdrive sync upload ./code/neuralgen 1-Pv6xsVhcskQW1FwcnO-KORytBM53gID
gdrive sync download 1-Pv6xsVhcskQW1FwcnO-KORytBM53gID ./code/neuralgen
```

> 本地删除的文件，以及服务器端删除的文件，在gdrive 云端不会删除（就假想成一条记录还在吧）
>
> 因此删除文件需要通过 gdrive delete <file-id> 来删除
>
> 上面的同步指令只能用来服务器端增加文件，以及双端修改文件





## 测试代码

使用 tmux 保证进程不被打断

```bash
# 开始
tmux

# 关闭
先按 `ctrl+b` ，全松开再按 `d`；或者输入 `tmux detach`

# 恢复
tmux attach -t 0

# 查看现存副终端列表
tmux ls
```







## 准备提交任务

**新键一个condor文件，例如myjob.condor，里面写入**

```bash
executable = myproc.sh 

requirements = (CUDADeviceName == "GeForce RTX 2080 Ti")  # 只对HTGC2有效
request_GPUs = 2          # 只对HTGC3有效

error      = myproc.err
log        = myproc.log
output     = htpc1.out

queue
```

**新键一个bash文件，例如myproc.sh ，里面写入**

```bash
#!/bin/bash

. "/home/grads/zhiyuyang4/anaconda3/etc/profile.d/conda.sh" # 调用conda

conda activate base

python train_gan.py configs/ditgraf/celebA_64_htgc2_1.yaml
```

> 注意修改上面的anaconda3 -》miniconda3



## Conder命令

```bash
# 查询服务器GPU空余状态
condor_status

# 提交任务
condor_submit myproc.condor

# 查询自己任务状态
condor_q

# 取消自己任务
condor_rm {Job ID}
```



> condor_q的状态有 IDLE, HOLD, RUN.



**其他命令**

```bash
condor_userprio # 查优先级和谁在用

condor_q -analyze 
condor_q -better-analyze

condor_history 

condor_q , tail

condor_q -global
```



**pipeline**

```bash
./rename.sh 01
```

./pro2_part/bin/topmg -i ./pro2_part/data/EC_variable_mods.txt ./pro2_part/data/EC_canonical.fasta ./pro2_part/data/BW_20_1_111106004325_cidetd_ms2.msalign 
