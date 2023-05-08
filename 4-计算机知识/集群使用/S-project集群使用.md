# S-project集群使用









srun -p shlab_adg --gres=gpu:1 --cpus-per-task=12 python utils/setup.py install --fix-lcuda



ln –s  /mnt/cache/yangzhiyuan/envs/nr3d/bin/x86_64-conda-linux-gnu-gcc /mnt/cache/yangzhiyuan/envs/nr3d/bin/gcc

ln –snf  /mnt/cache/yangzhiyuan/envs/nr3d/bin/x86_64-conda-linux-gnu-g++ /mnt/cache/yangzhiyuan/envs/nr3d/bin/g++



conda activate /mnt/cache/yangzhiyuan/envs/3d3



Solving environment: failed with initial frozen solve. Retrying with flexible solve.







pip install opencv-python icecream xmltodict makefun tqdm scikit-image pandas tensorboard addict imageio imageio-ffmpeg pyquaternion scikit-learn pyyaml seaborn PyMCubes trimesh plyfile omegaconf



rm -rf /mnt/cache/yangzhiyuan/envs/nr3d/bin/gcc

rm -rf /mnt/cache/yangzhiyuan/envs/nr3d/bin/g++

ln -s /mnt/cache/yangzhiyuan/envs/3d3/bin/x86_64-conda_cos6-linux-gnu-gcc /mnt/cache/yangzhiyuan/envs/3d3/bin/gcc1

ln -s /mnt/cache/yangzhiyuan/envs/3d3/bin/x86_64-conda_cos6-linux-gnu-g++ /mnt/cache/yangzhiyuan/envs/3d3/bin/g++



export CC=/mnt/cache/yangzhiyuan/miniconda3/envs/nr3d/bin/x86_64-conda-linux-gnu-gcc
export CXX=/mnt/cache/yangzhiyuan/miniconda3/envs/nr3d/bin/x86_64-conda-linux-gnu-g++





/mnt/cache/yangzhiyuan/envs/nr3d/bin/



gxx_linux-64

gcc_impl_linux-64 and gcc_linux-64 gxx_linux-64 



解决问题：

https://stackoverflow.com/questions/62999715/when-i-make-darknet-with-cuda-1-usr-bin-ld-cannot-find-lcudaoccured-how

"stub" libraries libcuda

https://github.com/conda-forge/nvcc-feedstock/issues/12

https://github.com/NVIDIA/nvidia-docker/issues/775

Add -lcuda to the command line to make the linker happy.

https://stackoverflow.com/questions/4385555/in-linux-stubs-are-used-for-standard-libraries-why-are-stubs-required

https://stackoverflow.com/questions/25643560/how-to-create-stub-shared-libraries-on-linux

https://stackoverflow.com/questions/39808924/how-stub-functions-in-c-are-used-are-replaced-by-shared-library-functions

https://github.com/NVIDIA/nvidia-docker/issues/775

libcuda.so in stubs



ln -s /mnt/cache/yangzhiyuan/miniforge3/bin/x86_64-conda-linux-gnu-gcc /mnt/cache/yangzhiyuan/miniforge3/bin/gcc

ln -s /mnt/cache/yangzhiyuan/miniforge3/bin/x86_64-conda-linux-gnu-g++  /mnt/cache/yangzhiyuan/miniforge3/bin/g++

echo "CC=/mnt/cache/yangzhiyuan/miniforge3/bin/x86_64-conda-linux-gnu-gcc" >> ~/.bashrc

echo "CXX=/mnt/cache/yangzhiyuan/miniforge3/bin/x86_64-conda-linux-gnu-g++" >> ~/.bashrc

echo "export CUDA_HOME=/mnt/lustre/share/cuda-11.3" >> ~/.bashrc

echo "export PATH=/mnt/lustre/share/cuda-11.3/bin:$PATH" >> ~/.bashrc







srun -p shlab_adg -n 1 --ntasks-per-node=1 --gres=gpu:1 --cpus-per-task=12 --kill-on-bad-exit=1 python -m train --config configs/stylelodneus_srn.yaml training.monitoring=none









srun -p shlab_adg -n 1 --gres=gpu:1 python -m debugpy --listen 0.0.0.0:27678 --wait-for-client train.py --config configs/yzy_adgan.yaml



重新run后，是加载的新数据，但



### neuralgen 调试

```shell
# step1:
srun -p shlab_adg --quotatype=auto --job-name=nr3d --gres=gpu:1 --cpus-per-task=12 python -m debugpy --listen 0.0.0.0:27678 --wait-for-client train.py --config configs/yzy_adgan.yaml

# step2: 查询你提交的节点IP
squeue -u <username>

# step3: 配置 vscode 调试json
{
    "name": "Debug",
    "type": "python",
    "request": "attach",
    "connect": {
        "host": "SH-IDC1-10-140-0-136",
        "port": 27678
    }
}
```



### neuralgen 运行

```shell
srun -p shlab_adg --quotatype=auto --job-name=nr3d --gres=gpu:1 --cpus-per-task=12 python train.py --config configs/yzy_adgan.yaml
```





srun -p shlab_adg --quotatype=auto --job-name=nr3d --gres=gpu:1 --cpus-per-task=12 python gen_samples.py --outdir=out --trunc=0.7 --shapes=true --seeds=0-3 --network=networks/afhqcats512-128.pkl

### neuralsim 运行

```shell
srun -p shlab_adg --job-name=nr3d --gres=gpu:1 --cpus-per-task=12 python -m tools.render.demo_category --mode interpolation --num_views 16 --num_frames_per_view 80 --camera_hwf "200, 200, 200" --from_neuralgen /mnt/lustre/yangzhiyuan/logs/latent_optimization/newnew
```



python tools/render/demo_category.py --mode interpolation --from_neuralgen /mnt/lustre/yangzhiyuan/logs/ 


srun -p shlab_adg --job-name=nr3d --gres=gpu:1 --cpus-per-task=12 python -m tools.render.demo_category --mode interpolation --num_views 16 --from_neuralgen /mnt/lustre/yangzhiyuan/logs/stylelodneus_srn/adgan_200sample_64pixel_lr0.0005_gan-weight_0.1



### Test

```python
srun -p shlab_adg --quotatype=auto --job-name=nr3d --gres=gpu:1 --cpus-per-task=12 python test.py
```



adgan_200sample_64pixel_lr0.0005_discriminator



srun -p shlab_adg --gres=gpu:1 --quotatype=auto --cpus-per-task=12 --kill-on-bad-exit=1 python gen_videos.py --outdir=/mnt/lustre/yangzhiyuan/exp_eg3d/latent/interface/eyeglass --trunc=0.7 --seeds=0-3 --grid=1x1 --shapes=false --network=./pretrained_models/ffhqrebalanced512-128.pkl







## 配置 S3 数据IO

alias labaws="aws s3 --endpoint-url=http://10.140.14.254:80"

labaws ls shared_3dnr/srn_car/cars_train/2228a428bfa91e4f771592b49641a847/



's3://shared_3dnr/srn_car/cars_train/2228a428bfa91e4f771592b49641a847/intrinsics.txt'



cp /mnt/lustre/share/pytcs/petrel_pymc.so ~/.local/lib/python3.9/site-packages/petrel_client/cache/mc/petrel_pymc.so



cp /mnt/lustre/share/pytcs/petrel_pymc.so /mnt/cache/yangzhiyuan/miniconda3/envs/nr3d/lib/python3.9/site-packages/petrel_client/cache/mc/petrel_pymc.so





cp /mnt/lustre/share/petrel-oss-python-sdk/petrel_client/cache/mc/petrel_pymc.so /mnt/cache/yangzhiyuan/miniconda3/envs/nr3d/lib/python3.9/site-packages/petrel_client/cache/mc/petrel_pymc.so



~/.local/lib/python3.9/site-packages/petrel_client/petreloss.conf

```python
from petrel_client.client import Client  
import cv2
import numpy as np

client = Client('~/petreloss.conf') # 若不指定配置文件，默认使用 ~/.petreloss.conf
input_img_url, output_url_jpg, output_url_jpg_gray = 'cluster1:s3://Demo/demo.png', 'cluster2:s3://Demo/demo.jpg', 'cluster2:s3://Demo/demo.gray.jpg'

input_img_bytes = client.get(input_img_url) # 得到远程文件的字节
assert input_img_bytes is not None

input_img_mem_view = memoryview(input_img_bytes) # 获取远程文件的内存
input_img_array = np.frombuffer(input_img_mem_view, np.uint8) # 将远程文件的内存表示转成np数组


img_ori = cv2.imdecode(input_img_array, cv2.IMREAD_COLOR) # 将png文件转成彩色jpg
img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY) # 将png文件转成灰度jpg

_, img_array = cv2.imencode('.jpg', img_ori) # 保存彩色jpg
_, img_gray_array = cv2.imencode('.jpg', img_gray) # 保存灰度jpg

client.put(output_url_jpg, img_array.tostring()) # 将彩色jpg转换成byte并上传到服务器
client.put(output_url_jpg_gray, img_gray_array.tostring()) # 将灰度jpg转换成byte并上传到服务器
```



```
client = Client('~/petreloss.conf')

input_img_bytes = client.get(input_img_url)


cat ceph_petreloss.log.d/slurm_procid_0.log
```



aws s3 --endpoint-url=http://10.140.2.254:80 ls s3://shared_3dnr/srn_car/... 



## 配置代理

```shell
alias proxy_on='export http_proxy=http://172.16.1.135:3128/;export https_proxy=http://172.16.1.135:3128/;export HTTP_PROXY=http://172.16.1.135:3128/;export HTTPS_PROXY=http://172.16.1.135:3128/'
alias proxy_off='unset http_proxy;unset https_proxy;unset HTTP_PROXY;unset HTTPS_PROXY'
```







先看每次加载的名字一致不

知道有Key，是数据集的对应信息，那么latent是什么呢？



使用nohup提交任务

压缩解压也用srun去做







conda actiavte siyuan



srun -p shlab_adg --quotatype=auto --gres=gpu:4 --cpus-per-task=48 python train.py --gpu 0,1,2,3 --save-path "./experiments/CIFAR_FS_MetaOptNet_SVM" --train-shot 15 --head SVM --network ResNet --dataset CIFAR_FS --eps 0.1
