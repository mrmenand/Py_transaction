## 逻辑斯谛回归与最大熵模型 
逻辑斯谛回归（logistic regression，判别模型）是统计学习中的经典**分类**方法，最大熵是概率模型学习的一个准则，将其推广到分类问题得到最大熵模型（maximum entropy model，生成模型）。（都属于**对数线性模型**） 

### 逻辑斯谛回归模型 


数学之美中有这样一个公式(**sigmoid**函数)
$$
f(z)=\color{red}\frac{e^z}{e^z+1}\color{black}=\frac{1}{1+e^{-z}}
$$
然后几率和概率之间的关系有这样一种表达
$$
o=\frac{p}{1-p} \\
\color{red}p=\frac{o}{1+o}
$$
看上面红色部分, **逻辑斯谛分布**对应了一种**概率**, **几率**为指数形式 $e^z$,  $z$ 为**对数几率(log odd)**.



$$
logit(p)=\log(o)=\log\frac{p}{1-p}
$$


### 

设：
$$P(Y=1|x)=\pi(x),P(Y=0|x)=1-\pi(x) \\
\pi(x) \in (0,1) 为条件概率  
$$ 
有逻辑斯谛分布：
$$
\log\frac{P(Y=1|x)}{1-P(Y=1|x)}=\log\frac{\pi(x)}{1-\pi(x)} =w\cdot x  \\
w\cdot x \in （- \infty,+\infty）是关系x的对数线性函数、
$$

故**二项逻辑斯谛回归模型**有：
$$
\begin{aligned}
P(Y=1|x)&=\frac{\exp(w\cdot x)}{1+\exp(w\cdot x)}\\
&=\frac{1}{e^{-(w\cdot x)}+1}\\
P(Y=0|x)&=\frac{1}{1+\exp(w\cdot x)}\\
&=\frac{e^{-(w\cdot x)}}{1+e^{-(w\cdot x)}}
\end{aligned}
$$

多项（二项）逻辑斯谛回归的模型(**与softmax的区别**)
$$
P(Y=k|x)=\frac{\exp(w_k\cdot x)}{\sum_{k=1}^{K}\exp(w_k\cdot x)} ，k=1,2,\dots,K
$$
有$w_K=0$表示负分类的参数 

### 最大熵模型 
最大熵原理(Maxent principle)是**概率模型**学习或者估计的一个准则。 

#### 熵 
假设离散随机变量$X$的概率分布是$P(X)$，则其熵为：
$$H(P)=-\sum_xP(x)\log{P(x)}$$ 满足下列不等式：
$$0\leq H(P) \leq log{|P(x)|}$$当$X$服从均匀分布时，熵最大。 

#### 最大熵模型的学习
最大熵模型的学习过程就是求解最大熵模型的过程。  

最大熵模型的学习可以形式化为**约束最优化问题**： 
$$min  -H(P)=\sum_{x,y}\hat{P(x)}P(y|x)\log{P(y|x)} \\ 
s.t. P(f_i)-\hat{P(x_i)}=0,i=1,2,\dots,n \\ 
\sum_yP(y|x)=1$$ 

通过求解**对数似然函数极大化**或者对偶函数极大化的问题，有最大熵模型一般形式：
$$
P_w(y|x)=\frac{1}{Z_w(x)}\exp{\sum\limits_{i=1}^{n}w_if_i(x,y)}\\
Z_w(x)=\sum_y\exp{\sum_{i=1}^{n}w_if_i(x,y)}
$$

注意这里面$Z_w$是归一化因子,$f_i$为特征函数，$w_i$为特征的权重。 


