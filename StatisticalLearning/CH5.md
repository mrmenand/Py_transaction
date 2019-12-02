## 决策树 
分类决策树模型是表示基于特征对实例进行的分类的树形结构，决策树可以换成一个**if-then**规则的集合，也可以看做是定义在特征空间划分上的**类条件概率分布**。 

## 算法 
包括三部分：**特征选择、树的生成和树的剪枝**。常用的算法有ID3、C4.5和CART

决策树的生成对应于模型的**局部选择**（局部最优），剪枝则考虑**全局最优**。
### 特征选择 
决定用那个特征划分特征空间。 
在各个节点上应用**信息增益最大**、**信息增益比最大**或者**基尼系数最小**作为特征选取准则。  

#### 样本集合D对特征A的信息增益（ID3） 
$$  
g(D,A)=H(D)-H(D|A) \\  
H（D） = -\sum_{k=1}^K\frac{|C_k|}{|D|}\log_2\frac{|C_k|}{|D|} \\   
H(D|A)=\sum_{i=1}^n\frac{|D_i|}{|D|}H(D_i)=-\sum_{i=1}^n\frac{|D_i|}{|D|}\sum_{k=1}^K\frac{|D_{ik}|}{|D_i|}\log_2\frac{|D_{ik}|}{|D_i|}$$ 

其中$H(D)$是数据集的熵，$H(D_i)$是数据$D_i$的熵$H(D|A)$是数据集$D$对特征$A$的条件熵。$D_i$是$D$中特征$A$取第$i$值的样本子集，$C_k$是D中属于第$k$类的样本子集。$n$是特征$A$取值的个数，$K$是类的个数。

#### 样本集合D对于特征A的信息增益比（C4.5） 
$$ g_R(D,A)=\frac{g(D,A)}{H_A(D)}\\
H_A(D)=-\sum_{i=1}^n\frac{D_i}{D}log_2\frac{D_i}{D}$$ 

其中$g_R(D,A)$是信息增益，$H_A(D)$是$D$关于特征$A$值的熵。 

#### 样本集合D的基尼指数（CART） 
$$
Gini(D) =1-\sum_{k=1}^K(\frac{{|C_k|}}{|D|})^2 
$$
特征A集合下D的基尼指数：
$$Gini(D,A)=\frac {|D_1|}{|D|}Gini(D1) + \frac {|D_2|}{|D|}Gini(D2)$$

### 决策树的生成 
从根节点开始，递归产生决策树。利用上述等准则不断选取**局部最优的特征**或者间将训练集分割为能够基本正确分类的子集。 

### 决策树剪枝 
过拟合的原因在于学习时过多地考虑如歌提高训练数据的正确分类，从而构建出过于复杂的决策树。

#### 剪枝算法
> 输入： 生成算法产生的整个树$T$,$t$是树的$T$的叶节点该结点有$N_t$个样本点，其中$k$类的样本点有$N_{tk}$个，$H_t(T)$为叶结点$t$上的经验熵， $\alpha\geq0$为参数。 
>
> 输出：修剪后的子树$T_{\alpha}$ 
> 1. 计算每个结点的经验熵 ： 
   $$H_t(T)=-\sum_k \frac{N_{tk}}{N_t}\log \frac{N_{tk}}{N_t} \\
   C(T)=\sum_{t=1}^{|T|}\color{red}N_tH_t(T)\color{black}=-\sum_{t=1}^{|T|}\sum_{k=1}^K\color{red}N_{tk}\color{black}\log\frac{N_{tk}}{N_t}$$ 
> 
> 1. 递归地从树的叶节点向上回溯。
$$C_\alpha(T)=C(T)+\alpha|T|$$
> 假设一组叶结点回缩到其父结点之前与之后的整体树分别是$T_B$和$T_A$，其对应的损失函数分别是$C_\alpha(T_A)$和$C_\alpha(T_B)$，如果$C_\alpha(T_A)\leq C_\alpha(T_B)$则进行剪枝，即将父结点变为新的叶结点 
>
> 1. 返回2，直至不能继续为止，得到损失函数最小的子树$T_\alpha$ 


### CART算法 
分类与回归树（classification and regresiion tree）既可以用于分类可以用于回归。 
对于回归树用**平方误差最小化准则**，对分类树用**基尼指数（Gini index）最小化准则**。 


#### 最小二乘回归树生成算法

递归地将每个区域划分为两个子区域并决定每个子区域的输出值，构建二叉决策树。 
> 输入：训练数据集$D$
> 
> 输出：回归树$f(x)$ 
> 
>1. 遍历变量$j$，对固定的切分变量$j$扫描切分点$s$，得到满足上面关系的$(j,s)$:
   $$
   \min\limits_{j,s}\left[\min\limits_{c_1}\sum\limits_{x_i\in R_1(j,s)}(y_i-c_1)^2+\min\limits_{c_2}\sum\limits_{x_i\in R_2(j,s)}(y_i-c_2)^2\right]
   $$
> 1. 对两个子区域调用(1)(2)步骤， 直至满足停止条件
> 1. 将输入空间划分为$M$个区域$R_1, R_2,\dots,R_M$，生成决策树：
   $$
   f(x)=\sum_{m=1}^M\hat{c}_mI(x\in R_m)
   $$ 

#### 分类树的生成 
如果样本集合$D$根据特征$A$是否取某一可能值$\alpha$被分割成$D1$和$D2$两部分，即
$$D_1= \{（x，y） \in D |A(x)=a\}, D2=D-D1$$
特征A集合下D的基尼指数：
$$Gini(D,A)=\frac {|D_1|}{|D|}Gini(D1) + \frac {|D_2|}{|D|}Gini(D2)$$

基尼指数$Gini(D)$表示集合$D$的不确定性，$Gini(D，A)$表示$A=a$分割后集合$D$的不确定性。