## EM算法及其推广  
EM算法是含有隐变量的概率模型极大似然估计或极大后验概率估计的迭代。 

### EM算法的引入 
用$Y$表示观测随机变量的数据，$Z$表示隐随机变量的数据。$Y$和$Z$一起称为**完全数据**(complete-data)，观测数据$Y$又称为**不完全数据**(incomplete-data)。

假设给定观测数据$Y$，其概率分布$P(Y|\theta)$,其中$\theta$是需要估计的模型参数，那么不完全的数据$Y$的对数似然函数$L(\theta)=\log{P(Y|\theta)}$,那么完全数据的对数似然函数是表示为$\log{P(Y,Z|\theta)}$。 

#### 三硬币模型 
$$
\begin{aligned}
    P(y|\theta)&=\sum_z P(y,z|\theta) \\
    &=\sum_z P(z|\theta)P(y|z,\theta) \\
    &=\pi p^y (1-p)^{1-y} + (1-\pi)q^y(1-q)^{1-y}
\end{aligned}
$$
以上

1. 随机变量$y$是观测变量，表示一次试验观测的结果是**1或0**
1. 随机变量$z$是隐变量，表示未观测到的掷硬币$A$的结果
1. $\theta=(\pi,p,q)$是模型参数
1. 这个模型是**以上数据**(1,1,0,1,0,0,1,0,1,1)的生成模型

观测数据表示为$Y=(Y_1, Y_2, Y_3, \dots, Y_n)^T$, 未观测数据表示为$Z=(Z_1,Z_2, Z_3,\dots, Z_n)^T$, 则观测数据的似然函数为：
$$
P(Y|\theta) = \sum\limits_{Z}P(Z|\theta)P(Y|Z,\theta)
$$
即：
$$
P(Y|\theta)=\prod\limits^{n}_{j=1}[\pi p^{y_j}(1-p)^{1-y_j}+(1-\pi)q^{y_j}(1-q)^{1-y_j}]
$$ 

考虑求模型参数$\theta=(\pi,p,q)$的极大似然估计, 即
$$
\hat \theta = \arg\max\limits_{\theta}\log P(Y|\theta)
$$  

#### 三硬币模型的EM算法

##### 1.初值

EM算法首选参数初值，记作$\theta^{(0)}=(\pi^{(0)},p^{(0)}, q^{(0)})$, 然后迭代计算参数的估计值。

如果第$i$次迭代的模型参数估计值为$\theta^{(i)}=(\pi^{(i)}, p^{(i)}, q^{(i)})$

##### 2.E步

那么第$i+1$ 次迭代的模型参数估计值表示为
$$
\mu_j^{i+1} = \frac{\pi^{(i)}(p^{(i)})^{y_j}(1-p^{(i)})^{1-y_j}}{\pi^{(i)}(p^{(i)})^{y_j}(1-p^{(i)})^{1-y_j} + (1-\pi^{(i)})(q^{(i)})^{y_j}(1-q^{(i)})^{1-y_j}}
$$
因为是硬币，只有0，1两种可能，所有有上面的表达。

这个表达方式还可以拆成如下形式
$$
\mu_j^{i+1} =
\begin{cases}
\frac{\pi^{(i)}p^{(i)}}{\pi^{(i)}p^{(i)} + (1-\pi^{(i)})q^{(i)}}&, y_j = 1\\
\frac{\pi^{(i)}(1-p^{(i)})}{\pi^{(i)}(1-p^{(i)}) + (1-\pi^{(i)})(1-q^{(i)})}&, y_j = 0\\
\end{cases}
$$
所以, 这步(求$\mu_j$)干了什么，样本起到了什么作用？

 这一步，通过假设的参数，计算了不同的样本对假设模型的响应($\mu_j$)，注意这里因为样本($y_j$)是二值的，所以，用$\{y_j, 1-y_j\}$ 构成了one-hot的编码，用来表示样本归属的假设。 

##### 3.M步

$$
\pi^{(i+1)} = \frac{1}{n}\sum_{j=1}^{n}\mu_j^{(i+1)}\\
p^{(i+1)} = \frac{\sum_{j=1}^{n}\mu_j^{(i+1)}y_j}{\sum_{j=1}^{n}\mu_j^{(i+1)}}\\
q^{(i+1)} = \frac{\sum_{j=1}^{n}(1-\mu_j^{(i+1)})y_j}{\sum_{j=1}^{n}(1-\mu_j^{(i+1)})} $$


EM算法与**初值**的选择有关，选择不同的初值可能得到不同的参数估计值。


#### EM算法 
输入: 观测变量数据$Y$，隐变量数据$Z$，联合分布$P(Y,Z|\theta)$，条件分布$P(Z|Y,\theta)$
 输出: 模型参数$\theta$

1. 选择参数的初值$\theta^{(0)}$，开始迭代  

1. E步：记$\theta^{(i)}$为第 $i$ 次迭代参数$\theta$的估计值，在第$i+1$次迭代的$E$步，计算：
$$
\begin{aligned}
   Q(\theta, \theta^{(i)}) = E_Z[\log P(Y,Z|\theta)|Y,\theta^{(i)}] \\
   = \sum_Z\log{P(Y,Z|\theta)}P(Z|Y, \theta^{(i)})
\end{aligned}
$$

3. M步
 求使$Q(\theta, \theta^{(i)})$最大化的$\theta$，确定第$i+1$次迭代的参数估计值
 $$
 \theta^{(i+1)}=\arg\max_\theta Q(\theta, \theta^{(i)})
 $$ 

#### Q函数  

完全数据的**对数似然函数$\log P(Y, Z|\theta)$关于**给定观测数据$Y$的当前参数$\theta^{(i)}$下对为观测数据$Z$的**条件概率分布$P(Z|Y,\theta^{(i)})$的期望**称为Q函数  

#### EM算法收敛性 
EM算法在每次迭代后均提高观测数据的似然函数值，即：
$$P(Y|\theta^{(i+1)}) \geq P(Y|\theta^{（i）})$$ 
在一般条件下EM算法是收敛的，但不同保证收敛到全局最优。 


### EM算法在高斯混合模型学习

#### 高斯混合模型 
高斯混合模型(Gaussian Mixture Model)是具有如下**概率分布**的模型:
$$
P(y|\theta)=\sum\limits^{K}_{k=1}\alpha_k\phi(y|\theta_k)
$$
其中，$\alpha_k$是系数，$\alpha_k\ge0$，$\sum\limits^{K}_{k=1}\alpha_k=1$, $\phi(y|\theta_k)$ 是**高斯分布密度**，$\theta_k=(\mu,\sigma^2)$
$$
\phi(y|\theta_k)=\frac{1}{\sqrt{2\pi}\sigma_k}\exp\left(-\frac{(y-\mu_k)^2}{2\sigma_k^2}\right)
$$
上式表示第k个**分**模型。 


#### 高斯混合模型参数估计的EM算法  
1. 取参数的的初始值开始迭代 
1. E步：依据当前模型参数，计算分模型$k$对观测数据的$y_i$的响应度 
$$
\hat y_{jk}=
\frac{\alpha_k\phi(y_j|\theta_k)}{\sum_{k=1}^K\alpha_k\phi(y_j|\theta_k)}
$$ 
3. M步：计算新一轮迭代的模型参数：
 $$
 \hat u_k = \frac {\sum_{j=1}^N \hat y_{jk}y_j}
  {\sum_i^N\hat y_{jk}} \\ 
 \hat \sigma_k^2 = \frac  {\sum_{j=1}^N\hat y_{jk}(y_j-\mu_k)^2} {\sum_{j=1}^N\hat y_{jk}} \\ 
 \hat \alpha_k = \frac {\sum_{j=1}^N\hat y_{jk}y_j} {N}   
 $$ 
4. 重复第2和第3步，直到收敛。 



### GEM 
每次迭代增加F函数值。 
// TODO 


