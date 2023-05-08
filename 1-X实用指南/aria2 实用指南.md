# aria2使用指南

https://aria2.github.io/

> 好处是 多连接下载，轻量，支持bit，断点续传



download:

```bash
aria2c xxx

# Download URIs found in text file:
aria2c -i uris.txt
```

https://scontent-hkg4-1.xx.fbcdn.net/m1/v/t6/An8XvLDEMqb-BTRh8P8GTLACcot7UbhvyT5CEQwkCISoAMzxSFKYekeFQsgz4gshsD5MQjpDd8Z3e6k.zip?ccb=10-5&oh=d9172073a180902ec91d6f2e8946a0c8&oe=6151D181&_nc_sid=857daf





imagenet



```
aria2c --file-allocation=none -c -d F:/data http://www.image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar
```



