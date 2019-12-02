## 提升方法 
提升（boosting）方法是**弱**学习算法提升到**强**学习算法的的统计学习方法。
在分类学习中，提升方法通过反复的修改训练数据的权值分布，构建一系列的弱分类器并进行**线性组合**。  


### Adaboost算法 
概率近似正确(PAC, Probably approximately correct)

在PAC学习框架下，一个概念是强可学习的**充分必要条件**是这个概念是弱可学习的。
两个问题

1. 在每一轮如何改变训练数据的权值或者概率分布
1. 如何将弱分类器组合成一个强分类器

Adaboost解决方案：
1. 提高前一轮被分错的分类样本的权值，降低被正确分类的样本的权值
1. 加权多数表决的方法  

一些问题：
- 不同的权值分布上，不同样本错分对评价结果d的贡献不同，**分类器**中分类错误的会被放大，分类正确的系数会减小，错误和正确的系数比值为$e^{2\alpha_m}=\frac{1-e_m}{e_m}$，这个比值是分类器分类正确的**几率**($odds$)
 
- AdaBoost的两个性质：
  - 能在学习过程中不断减少训练误差
  - 训练误差是以指数速率下降的 



算法如下：

* 输入：训练数据集$T=\{(x_1,y_1), (x_2,y_2),...,(x_N,y_N)\}, x\in  \mathcal X\subseteq \R^n$, 弱学习方法
* 输出：最终分类器$G(x)$

步骤
1. 初始化训练数据的权值分布 $D_1=(w_{11},\cdots,w_{1i},\cdots,w_{1N},w_{1i}=\frac{1}{N})​$
1. m = 1,2, M
    1. $G_m(x):X \rightarrow \{-1,+1\}$
    1. 求$G_m$在训练集上的分类误差率  $e_m=\sum_{i=1}^{N}P(G_m(x_i)\ne y_i)=\sum_{i=1}^{N}w_{mi}I(G_m(x_i)\ne y_i)$
    1. 计算$G_m(x)$的系数，$\alpha_m=\frac{1}{2}log\frac{1-e_m}{e_m}$，自然对数
    1. $w_{m+1,i}=\frac{w_{mi}}{Z_m}exp(-\alpha_my_iG_m(x_i))​$
    1. $Z_m=\sum_{i=1}^Nw_{mi}exp(-\alpha_my_iG_m(x_i))$
1. $f(x)=\sum_{m=1}^M\alpha_mG_m(x)$
1. 最终分类器$G(x)=sign(f(x))=sign(\sum_{m=1}^M\alpha_mG_m(x))$  

### AdaBoost 误差分析 
AdaBoost算法最终分类器的训练误差界为
$$
\frac{1}{N}\sum\limits_{i=1}\limits^N I(G(x_i)\neq y_i)\le\frac{1}{N}\sum\limits_i\exp(-y_i f(x_i))=\prod\limits_m Z_m
$$
// TODO 不是很懂 


### AdaBoost 算法的解释 
模型为加法模型，损失函数为指数函数，学习算法为前向分布算法时二类分类学习方法。  


输入：训练数据集$T={(x_1,y_1),(x_2,y_2),...,(x_N, y_N)}, x_i \in \mathcal X \sube R^n, y_i\in \{-1, 1\}$， 损失函数$L(y, f(x))$; 基函数集合$\{b(x;\gamma)\}$

输出：加法模型$f(x)$

步骤：

1. 初始化$f_0(x)=0$
1. 对$m=1,2,\dots,M$
1. 极小化损失函数
   $$
   (\beta_m,\gamma_m)=\arg\min \limits_ {\beta,\gamma}\sum_{i=1}^NL(y_i, f_{m-1}(x_i)+\beta b(x_i;\gamma))
   $$

1. 更新
   $$
   f_m(x)=f_{m-1}(x)+\beta _mb(x;\gamma_m)
   $$

1. 得到加法模型
   $$
   f(x)=f_M(x)=\sum_{m=1}^M\beta_m b(x;\gamma_m)
   $$ 

### 提升树 
以决策树为基函数的提升方法为提升树。

提升树模型可以表示成决策树的加法模型：
$$
f_M(x)=\sum_{m=1}^MT(x;\Theta_m)
$$ 
其中$T(x;\Theta_m)$表示决策树，$\Theta_m$为决策树的参数，$M$为树的个数。 


不同的问题， 主要区别在于损失函数不同：

1. 平方误差用于回归问题
1. 指数损失用于分类问题 


#### 回归问题的提升树算法 
1. 初始化$f_0(x)=0$
1. 对$m=1,2,\dots,M$
   1. 计算残差
   $$
   r_{mi}=y_i-f_{m-1}(x_i), i=1,2,\dots,N
   $$
   1. **拟合残差**$r_{mi}$学习一个回归树，得到$T(x;\Theta_m)$
   1. 更新$f_m(x)=f_{m-1}(x)+T(x;\Theta_m)$
1. 得到回归问题提升树
   $$
   f(x)=f_M(x)=\sum_{m=1}^MT(x;\Theta_m)
   $$

### 梯度提升(GBDT)

#### 算法8.4
输入： 训练数据集$T={(x_1,y_1),(x_2,y_2),\dots,(x_N,y_N)}, x_i \in \mathcal x \subseteq \R^n, y_i \in \mathcal y \subseteq \R$；损失函数$L(y,f(x))$
输出：回归树$\hat{f}(x)$

步骤：
1. 初始化
   $$
   f_0(x)=\arg\min\limits_c\sum_{i=1}^NL(y_i, c)
   $$

1. $m=1,2,\dots,M$
    > 1. $i=1,2,\dots,N$
     $$
    r_{mi}=-\left[\frac{\partial L(y_i, f(x_i))}{\partial f(x_i)}\right]_{f(x)=f_{m-1}(x)}
    $$
    > 1. 对$r_{mi}$拟合一个回归树，得到第$m$棵树的叶节点区域$R_{mj}, j=1,2,\dots,J$
    > 1. $j=1,2,\dots,J$
    $$
    c_{mj}=\arg\min_c\sum_{xi\in R_{mj}}L(y_i,f_{m-1}(x_i)+c)
    $$
    > 1. 更新
    $$
    f_m(x)=f_{m-1}(x)+\sum_{j=1}^Jc_{mj}I(x\in R_{mj})
    $$

1. 得到回归树
   $$
   \hat{f}(x)=f_M(x)=\sum_{m=1}^M\sum_{j=1}^Jc_{mj}I(x\in R_{mj})
   $$










