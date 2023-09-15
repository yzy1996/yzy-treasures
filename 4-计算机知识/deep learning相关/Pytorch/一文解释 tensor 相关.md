# 一文解释 tensor 相关

[toc]

#### Tensor 和 Numpy 互转

> 1. numpy to tensor

```python
a = np.random.randn(2)

# as_tensor是浅拷贝，数据是共享的，因此修改b也会修改a，需要注意
b = torch.as_tensor(a).float()

# 如果不想a, b互相影响，则可以采用
c = torch.tensor(a).float()

# 另外，如果需要转到 GPU，as_tensor也可以使用，因为只有cpu上的数据是共享的
d = torch.as_tensor(a).float().cuda()


torch.from_numpy(np_array)
```



> 2. tensor to numpy  

```python
a = torch.tensor(2.).cuda().requires_grad_()

b = a.detach().cpu().numpy()

# 这里可以发现很严谨的一点是，tensor是先到gpu再让求梯度，回到numpy是先去掉梯度再到cpu
# 如果是在计算图里 则需要 .detach()
# 如果是在GPU上，则需要 .cpu()
# 否则直接 .numpy()
```



#### Tensor 在 CPU 和 GPU 互转

这一点很简单，一般指令就是 `.cuda()`，`.to(device)`，其中 `device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")`

warning：记得一定是先 cuda，再requires_grad_()



#### Tensor 变数据类型

直接要什么数据类型就在最后加上什么

```python
a = torch.tensor(1., dtype=torch.double).float()
# output dtype=float32
```

如果是对于整个model而言的话是：

model.to(torch.double)



#### 初始化

```python
x = torch.randn(4, 4) # 正态分布
x = torch.rand(4, 4) # 均匀分布
x = torch.zeros(4, 4)
x = torch.ones(4, 4)
x = torch.tensor(4)
x = torch.arange(4)
x = torch.linspace(-10, 10, steps=5)

x = torch.zeros(5, 5).uniform_(-0.5, 0.5) # 得到的其实是一个均匀分布
```



### 查看size

```python
xx.size()
```



### 尺寸变换

```python
xx.view()
xx.reshape()

# view + contigious == reshape
```



### 维度变换

使用einops

```python
# 数据不变，增加一维

# 交换维度
x = torch.randn(2, 3, 5)
x.size()
>>> torch.Size([2, 3, 5])
x.permute(2, 0, 1).size()
>>> torch.Size([5, 2, 3])

# 减小维度
# 去掉“维数为1”的的维度
x.squeeze() # 括号内也可以跟某一维度

# 增加维度
x.unsqueeze(0) # 在最开头增加一维

# 扩展维度
x.expand((3,4)) # 将原本（3，1）变到 （3，4）

tile

# 交换维度
movedim(-1,0)

permute
transpose

transpose与permute的异同

'''
input = size(3, 3)
input.unsqueeze(0).unsqueeze(0) == input.expand(1, 1, 3, 3)
'''
拼接
cat
stack

拆分
chunk
split

[*[1]*2] = [1, 1]
[[1]*2] = [[1, 1]]
[1]*2 = [1, 1]

[[1]*2,2] =[[1, 1], 2]
[*[1]*2,2] = [1, 1, 2]
```



### 加减乘除

$\otimes$ 张量乘

**矩阵乘法**

```python
torch.mm
torch.bmm
torch.matmul

torch.mul
```

前三个等价于 `@` 操作符，最后一个等价于 `* ` 操作符





### Embed 初始化

```python
embd = nn.Embedding(5, 10)

# 访问
idx = torch.tensor([1, 2])
embd(idx)

# 查看权重，也就是具体数值
embd.weight.detach().numpy()

# 修改初始化权重
embd1.weight.data.normal_(1, 1) # 由N(0,1)改为N(1, 1)
```



类似于 list.append() 的拼接操作，逐步增加，

```python
a = [] 
for _ in range(2):
	b = ..
	b.unsqueeze_(1)
	a.append(b)
```





one layer with input size:
$$
(N, C, H, W)
$$
where N is a batch size, C denotes a number of channels, H is a height of input planes in pixels, and W is width in pixels.



kernel的组成



### 网络参数

self.named_parameters() ｜ self.parameters()

前者给出网络层的名字和参数的迭代器，而后者仅仅是参数的迭代器。

```python
import torchvision.models as models

model = models.mobilenet_v3_small()

# 前者给出网络层的名字和参数的迭代器，而后者仅仅是参数的迭代器。
out1 = next(model.named_parameters())
out2 = next(model.parameters())

out1[1][1] == out2[1] # True



for name, param in model.named_parameters():
    print(name, param)
    
for name, param in model.state_dict().items():
    print(name, param.size())
```



还有一个 model._parameters





for name, param in model.state_dict().items():
    print(name, param.size())





model.state_dict()其实返回的是一个OrderDict，存储了网络结构的名字和对应的参数

只有那些参数可以训练的layer才会被保存到模型的state_dict中,如卷积层,线性层等等，像什么池化层、BN层这些本身没有参数的层是没有在这个字典中的；

这个方法的作用一方面是方便查看某一个层的权值和偏置数据，另一方面更多的是在模型保存的时候使用。

优化器对象Optimizer也有一个state_dict,它包含了优化器的状态以及被使用的超参数(如lr, momentum,weight_decay等)





https://discuss.pytorch.org/t/issue-using-parameters-internal-method/134549/11

```python
module._parameters[param_key] = memo[p]

# Can become
delattr(module, param_key)
setattr(module, param_key, memo[p])
```







在pytorch中模型需要保存下来的参数包括：

parameter：反向传播需要被 optimizer 更新的，可以被训练。
buffer：反向传播不需要被 optimizer 更新，不可被训练。
 
这两种参数都会分别保存到 一个OrderDict 的变量中，最终由 model.state_dict() 返回进行保存。







nn.Module

```python
成员变量：

_buffers：由self.register_buffer() 定义，requires_grad默认为False，不可被训练。
_parameters：self.register_parameter()、nn.parameter.Parameter()、nn.Parameter() 定义的变量都存放在该属性下，且定义的参数的 requires_grad 默认为 True。
_modules：nn.Sequential()、nn.conv() 等定义的网络结构中的结构存放在该属性下。
 
成员函数：

self.state_dict()：OrderedDict 类型。保存神经网络的推理参数，包括parameter、buffer
self.name_parameters()：为迭代器。self._module 和 self._parameters中所有的可训练参数的名字+tensor。包括 BN的 bn.weight、bn.bias。
self.parameters()：与self.name_parameters()一样，但不包含名字
self.name_buffers()：为迭代器。网络中所有的不可训练参数和自己注册的buffer 中的参数的名字+tensor。包括 BN的 bn.running_mean、bn.running_var、bn.num_batches_tracked。
self.buffers()：与self.name_buffers()一样，但不包含名字
net.named_modules()：为迭代器。self._module中定义的网络结构的名字+层
net.modules()：与self.named_modules()一样，但不包含名字

```

