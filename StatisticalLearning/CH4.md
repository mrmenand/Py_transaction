### 朴素贝叶斯法（naive Bayes）
基于贝叶斯定理与特征条件独立假设的分类方法。  


#### 算法 
对于给定数据集$T$,基于**输入特征IID**学习输入输出的联合概率分布$P(X,Y)$，然后对于输入$x$利用贝叶斯定理求出后验概率最大的输出$y$ 
> 输入 ：$T =\{(x_1,y_1),(x_2,y_2),\dots,(x_N，y_N),x_i =(x_i^{(1)},x_i^{(2)},\dots,x_i^{(n)})^T,x_i^{(j)}是第i个样本的第j个特征，x_i^{(j)} \in \{a_{j1},a_{j2},\dots,a_{jS_j}\},a_{jl}是j个特征的可能取的第l个值，j=1,2,\dots,n;l=1,2,\dots,S_j；y_i \in \{c_1,c_2,\dots,c_K\};实例x$ 
> 
> 输出： 实例$x$的分类
>
>  1. 计算先验概率及条件概率
    $$ P(Y=c_k)= \frac{\sum_i^NI(y_i=c_k)}{N} ，k=1,2,\dots,K \\
    P（X^{(j)}=a_{jl}|Y=c_k）= \frac {\sum_i^nI(x_i^{(j)}=a_{jl},y_i=c_k)} {\sum_i^nI(y_i=c_k)}  $$
>
> 1. 对于给定实例$x=(x_i^{(1)},x_i^{(2)},\dots,x_i^{(n)})^T$,计算（联合概率分布$P(X,Y$） 
 $$P(Y=c_k)\prod_{j=1}^NP(X^{(j)}=x^{(j)}|Y=c_k),k=1,2,\dots,K $$  
>
> 1. 确定实例x的类 
  $$y=argmax_{c_k}P(Y=c_k)\prod_{j=1}^NP(X^{(j)}=x^{(j)}|Y=c_k)$$  


####　条件独立假设（IID）
- 条件概率分布$P(X=x|Y=c_k)$有指数级数量的参数，其实际估计是不可行的。 
- 用于分类的特征在类确定的条件下都是条件独立的 
- $$\begin{aligned}
P(X|Y)&=P(X_1,X_2|Y)\\
&=\color{red}P(X_1|X_2,Y)\color{black}P(X_2|Y)\\
&=\color{red}P(X_1|Y)\color{black}P(X_2|Y)
\end{aligned}
$$ 

#### 极大似然估计

> 为了估计状态变量的条件分布，利用贝叶斯法则，有
> $$
>    \underbrace{P(Y|X)}_{posterior}=\frac{\overbrace{P(X|Y)}^{likelihood}\overbrace{P(Y)}^{prior}}{\underbrace{P(X)}_{evidence}}=\frac{\overbrace{P(X|Y)}^{likelihood}\overbrace{P(Y)}^{prior}}{\underbrace{\sum\limits_x P(X|Y)P(Y)}_{evidence}}
> $$
> 其中$P(Y|X)$为给定$X$下$Y$的后验概率(Posterior)， $P(X|Y)$称为似然(Likelyhood)，$P(Y)$称为先验(Prior。
>

- 后验概率最大化的含义

  朴素贝叶斯法将实例分到**后验概率最大的类**中， 这等价于**期望风险最小化**。

- 后验，观察到$Y$之后，对$X$的信念
