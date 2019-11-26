### 感知机 
感知机（perceptron）是线性二分类模型

#### 模型 
输入（特征）空间 ： $\mathcal X \sube R^n $ 
输出空间 ：$\mathcal Y={+1,-1}$ 
决策函数(判别模型) ：$f(x)=sign (w\cdot x+b)$ 

#### 策略 
- 数据集的线性可分性 
  - 算法的收敛性：$k \leq (\frac R r )^2$ 
  - 误分类的次数$k$是有上界的，经过有限次的搜索可以找到将训练数据完全正确分开的分离的超平面  

- 经验风险函数（损失函数） 
  - $L(w,b)=-\sum_{x_i\in M}y_i(w\cdot x_i+b)$，其中M为误分类点的集合  
  - $\nabla_wL(w,b)= -\sum_{x_i \in M}y_ix_i$
  - $\nabla_bL(w,b)= -\sum_{x_i \in M}y_i$

#### 算法 
 - 原始形式
> 输入 ：训练数据集 $ =\{（x_1,y_1）,(x_2,y_2),\dots,(x_N,y_N)\}$,其中$x_i \in R^n,y_i \in \mathcal Y=\{1,-1\},i=1,2,\dots,N;学习率\eta(0\lt\eta\leq1)$ 
> 
> 输出 :$w,b;感知机模型f(x)=sign(w\cdot x+b)$ 
> 
> 1. 选取初值$w_0,b_0$
>
> 1. 训练集中选取数据$(x_i,y_i)$
>
> 1. 如果$y_i(w\cdot x_i+b)\leq 0$, 
    $$
    w \leftarrow w+\eta y_ix_i \\
    b\leftarrow b+\eta y_i
    $$
> 1. 转至(2)，直至训练集中没有误分类点


- 对偶形式 
 > $$
    f(x)=sign\left(\sum_{j=1}^N\alpha_jy_jx_j\cdot x+b\right) \\ 
    \alpha_i \leftarrow \alpha_i + \eta \\
    b \leftarrow b + \eta y_i $$


