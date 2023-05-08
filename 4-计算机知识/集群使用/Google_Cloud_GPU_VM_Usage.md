# 使用Google Cloud的GPU服务器

官方网址是：https://cloud.google.com/

教程说明：https://cloud.google.com/compute/docs/quickstart-linux



需要明确：

- 新用户有300刀的免费额度
- 体验用户最多只能申请一个V100-16G的GPU



### 申请配额

先绑定一个信用卡，升级为付费账户

然后申请一个V100配额，秒审批，但也只能申请一个



### 创建云端虚拟机

这有一个[官方教程](https://cloud.google.com/compute/docs/gpus/create-vm-with-gpus)，我这里只记几步重要

**机器系列**选GPU -> **系列**选N1 -> **机器类型**选CPU核心数和内存 -> **GPU类别**选V100 -> **启动磁盘**选系统和硬盘大小 -> 允许HTTP流量



创建好后点ssh连接就会打开一个谷歌加密的终端 （如果想用其他ssh软件，需要配密码登录，没有需求可以就算了）



### 文件传输

使用自带ssh终端上传和下载速度非常缓慢，借助[cloud storage](https://cloud.google.com/storage/docs/quickstart-console?hl=zh_CN)会快很多，相当于是一个中转

首先在网页上新键一个存储区，命个名字



本地到服务器：直接通过网页的上传按钮从本地传到cloud storage，然后执行以下命令从cloud storage到google vm，[命令教程](https://cloud.google.com/storage/docs/quickstart-gsutil)

```bash
gsutil cp gs://zhiyuan/test.txt ~/
```

服务器到本地：先从google vm到cloud storage，再从cloud storage下载到本地

```bash
gsutil cp ~/test.txt gs://zhiyuan
```



> 记住存储是要付费的，虽然不贵，但还是记得不用了之后就删除关闭服务，新建是很快的



### 参考文档

注意事项

https://cloud.google.com/compute/docs/ssh-in-browser?hl=zh-CN#copypaste

申请配额

https://cloud.google.com/compute/quotas?hl=zh-cn

