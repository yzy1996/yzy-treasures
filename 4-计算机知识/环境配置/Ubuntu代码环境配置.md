### Configure Ubuntu Environment



**安装 cuda** [参考链接](https://zhuanlan.zhihu.com/p/79059379)

验证gcc是否已经安装

```bash
gcc --version
```

没有就一次性安装 gcc make gcc++

```bash
sudo apt update
sudo apt install gcc g++ make
sudo apt install libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev freeglut3-dev
```

下载安装合适版本的[CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive)

> 注意cuda 11才开始支持ubuntu 20.04。就安装最新的cuda，pytorch是支持的。

```bash
# 样例不是最新可以替换
wget https://developer.download.nvidia.com/compute/cuda/11.2.1/local_installers/cuda_11.2.1_460.32.03_linux.run
sudo sh cuda_11.2.1_460.32.03_linux.run
```

安装完会输出cuda目录，把它添加到环境变量

```bash
nano ~/.bashrc
export PATH=$PATH:/usr/local/cuda-10.2/bin # 替换你对应的
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.2/lib64

打开新的终端或者 
source ~/.bashrc 生效
```

**安装 cudnn**

到 [cudnn](https://developer.nvidia.com/rdp/cudnn-download) 选择合适版本下载，并按 [官方指示](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)



**安装 Anaconda**

下载，最新[下载链接](https://www.anaconda.com/products/individual)，替换下面的

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh
source ~/.bashrc # 或者重启终端
```



**安装PyTorch** [官方](https://pytorch.org/get-started/locally/)选择合适版本

```bash
# 类似于
pip install torch torchvision torchaudio
```



**代码部分**

clone整个[仓库](https://github.com/ventusff/DIT-NERF)

```bash
git clone --recurse-submodules https://github.com/ventusff/DIT-NERF.git
```

**安装package**

```bash
# 必须
pip install tqdm scikit-image opencv-python pandas tensorboard tensorboardX addict imageio imageio-ffmpeg pyquaternion pyyaml
# 可选
pip install pynvml
```

**安装torch-batch-svd**

```
cd torch-batch-svd
export CUDA_HOME=/usr/local/cuda # 替换你对应的
python setup.py install
cd ..
```

每次运行前，在项目根目录下运行这个脚本来将当前路径临时添加到 `PYTHONPATH` 变量

```bash
source set_env.sh
```



**数据集**

- carla

- chair

- car

- celebA

- celebA-HQ











