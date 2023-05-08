# 利普希茨连续性 (Lipschitz Continuity)



主要公式

存在常数K，使得
$$
\|D(x)-D(y)\| \leq K\|x-y\|
$$
对于实数
$$
\frac{f(x)-f(y)}{x-y} \leq K
$$
最小的K被称为利普希茨常数

> 注意不需要可导



## 例子

- $f(x) = x^2$ 在定义域 $R$ 上不满足利普希茨条件，在有限定义域上满足
- $f(x) = \sqrt{x^2+5}$ 满足利普希茨条件， $K=1$
- $f(x) = |x|$ 满足利普希茨条件， $K=1$







1-Lipschitz activation functions (e.g., ReLU) 





A dominant strategy to achieve Lipschitz regularization is to perform weight normalization.



or instance, if one wants to enforce the network to be 1-Lipschitz 𝑐 = 1, then one can achieve this by normalizing the weight such that ∥W𝑖 ∥𝑝 = 1 after each gradient step during training.


$$
\begin{gathered}
\|M\|_2=\sigma_{\max }(\mathrm{M}), \\
\|\mathrm{M}\|_1=\max _j \sum_i\left|m_{i j}\right|, \\
\quad\|M\|_{\infty}=\max _i \sum_j\left|m_{i j}\right|,
\end{gathered}
$$
where 𝜎_max (M) denotes the maximum eigenvalue of M. Thus, when 𝑝 = 2, weight normalization consists of rescaling the weight matrix based on its maximum eigenvalue. Other popular techniques include spectral normalization based on the power iteration and the Björck Orthonormalization. When 𝑝 = ∞ (𝑝 = 1), weights normalization is simply scaling individual rows (columns) to have a maximum absolute row (column) sum smaller than a prescribed bound.
$$
\begin{aligned}
& \frac{1}{\sqrt{n}}\|M\|_{\infty} \leq\|M\|_2 \leq \sqrt{m}\|M\|_{\infty} \\
& \frac{1}{\sqrt{m}}\|M\|_1 \leq\|M\|_2 \leq \sqrt{n}\|M\|_1
\end{aligned}
$$



$$
\mathrm{y}=\sigma\left(\widehat{\mathrm{W}}_i \mathrm{x}+\mathrm{b}_i\right), \quad \widehat{\mathrm{W}}_i=\text { normalization }\left(\mathrm{W}_i \text {, softplus }\left(c_i\right)\right)
$$
here the softplus (𝑐_𝑖) = ln(1+𝑒^(c_i) ) is a reparameterization designed to avoid infeasible negative Lipschitz bounds.





```python
import jax.numpy as jnp

def normalization(Wi, softplus_ci): # L-inf norm
  absrowsum = jnp.sum(jnp.abs(Wi), axis=1)
  scale = jnp.minimum(1.0, softplus_ci/absrowsum)
  return Wi * scale[:,None]

## and each layer of the Lipscthiz MLP is simply
y = sigma(normalization(Wi, softplus(ci))*x + bi)

## where sigma denotes the activation function and softplus is the
## built-in softplus function in JAX.
```



- [Adversarial Lipschitz Regularization](https://arxiv.org/abs/1907.05681)  
  **[`ICLR 2020`]** *Dávid Terjék*
- 





一开始，使用explicit Lipschitz penalty是不切实际的？

在GAN里面Wasserstein distance estimation requires the function space of the critic to only consist of1-Lipschitz functions.

其实是gradient norm penalization，也有很多后续工作

本文提出 **enablingthe training of neural networks with regularization terms penalizing the violation of theLipschitz constraint explicitly, instead of through the norm of the gradient.**





Learning Smooth Neural Functions via Lipschitz Regularization





这里我们来看它是如何让Neural Fields变得平滑的





有entropic regularization 的dual问题是smooth的。