## 支持向量机 
支持向量机是一种二类分类模型。基本模型是定义在特征空间上的**间隔最大**的线性分类器。 
- 线性**可分**支持向量机 
  - 硬间隔最大化 
  - 直接求$w^*,b^*$ 
  - 学习的对偶算法，求$\alpha$进一步求$w^*,b^*$ 
- 线性支持向量机 
  - 软间隔最大 
  - 增加超参$C$，求$\alpha$进一步求$w^*,b^*$ 
- 非线性支持向量机 
  - 进一步引入核函数$K(x,z)$，求$\alpha$进一步求$b^*$  


### 线性可分支持向量机与硬间隔最大化 

#### 函数间隔 
对于给定数据集$T$和超平面$(w,b)$，定义超平面$(w,b)$关于样本点$(x_i,y_i)$的函数间隔为
$$
\hat \gamma_i=y_i(w\cdot x_i+b)
$$
定义超平面$(w,b)$关于训练数据集$T$的函数间隔为超平面$(w,b)$关于$T$中所有样本点$(x_i,y_i)$的函数间隔之最小值，即
$$
\hat \gamma=\min_{i=1,\cdots,N}\hat\gamma_i
$$
函数间隔可以表示分类预测的**正确性**及**确信度**。

#### 几何间隔 

$$ \gamma_i=y_i(\frac {w} {||w||} \cdot x_i+ \frac {b} {{||w||}}) $$ 

#### 间隔最大化（几何间隔） 
对训练数据集找到几何间隔最大化的分离超平面，表示约束最优化问题：
$$
max_{w,b} \quad \hat{\gamma}  \\
s.t. \quad y_i(w\cdot x_i+b) \geq \hat{\gamma} ,i=1,2,\dots,N  $$

等价的**线性可分支持向量机**最优化问题（凸二次规划问题）如下：
$$ min_{w,b} \quad \frac 1 2{||w||}^2  \\
s.t. \quad y_i(w\cdot x_i+b) -1 \geq 0 ,i=1,2,..N  
$$

故**线性可分的SVM**算法如下：

求出了上述方程的解$w^*, b^*$，就可得到

分离超平面（**存在且唯一**）
$$ w^*\cdot x+b^*=0 $$
相应的分类决策函数 
$$f(x)=sign(w^*\cdot x+b^*)$$ 

#### 学习的对偶算法 
针对每个不等式约束，定义拉格朗日乘子$\alpha_i\geq0​$，定义拉格朗日函数 
$$
L(w,b,\alpha) = \frac{1}{2}w\cdot w-\left[\sum_{i=1}^N\alpha_i[y_i(w\cdot x_i+b)-1]\right]\\
=\frac{1}{2}\left\|w\right\|^2-\left[\sum_{i=1}^N\alpha_i[y_i(w\cdot x_i+b)-1]\right]\\
=\frac{1}{2}\left\|w\right\|^2-\sum_{i=1}^N\alpha_iy_i(w\cdot x_i+b)+\sum_{i=1}^N\alpha_i
$$ 
其中$\alpha=(\alpha_1,\alpha_2,\dots,\alpha_N)^T​$为拉格朗日乘子向量。 

先求$L(w,b,\alpha)对w,b求极小，再求\alpha的极大$有等价的对偶最优化问题：

$$
\min\limits_\alpha \frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N\alpha_i\alpha_jy_iy_j(x_i\cdot x_j)-\sum_{i=1}^N\alpha_i\\
s.t. \ \ \ \sum_{i=1}^N\alpha_iy_i=0\\
\alpha_i\geqslant0, i=1,2,\dots,N
$$ 

求解上述方程的解$w^*, b^*$，
有：
 $$
 w^* =\sum_{i=1}^{N}\alpha_i^*y_ix_i \\
 b^* =y_j\color{black}-\sum_{i=1}^{N}\alpha_i^*y_i(x_i\cdot x_j) 
 $$ 
分离超平面：
  $$
  \sum_{i=1}^N a_i^*y_i(x \cdot x_i) + b^* = 0  
  $$ 
分类决策函数：
$$f(x)=sign(\sum_{i=1}^N a_i^*y_i(x \cdot x_i)+b^*)$$

$\alpha$不为零的点对应的实例为支持向量，通过支持向量可以求得$b$值 

### 线性支持向量机 
对每个样本点引进一个松弛变量$\xi_i\geq0$使其 **“可分”**，得到线性支持向量机的凸二次优化问题，其原始的优化问题如下 ：
$$ 
\min_{w,b,\xi} \quad \frac{1}{2}\left\|w\right\|^2+C\sum_{i=1}^N\xi_i \\ 
s.t. \quad y_i(w\cdot x_i+b)\geq 1 -\xi_i, i=1,2,\dots,N \\
\xi_i\geq0,i=1,2,\dots,N
$$


#### 对偶问题 
$$
\min_\alpha \quad \frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N\alpha_i\alpha_jy_iy_j(x_i\cdot x_j)-\sum_{i=1}^N\alpha_i \\
s.t.\quad \sum_{i=1}^N\alpha_iy_i=0 \\
0\leq \alpha_i \leq C,i=1,2,\dots,N
$$ 
通过对偶问题得到最优解$\alpha^*$,然后求原始问题最优解$w^*,b^*$,（其中$w^*$唯一但$b^*$不一定唯一）得出分离超平面和分类决策函数。

等价的最小化二阶范数正则化的合页函数 ：
$$
\min\limits_{w,b} \sum\limits_{i=1}^N\left[1-y_i(w\cdot x+b)\right]_++\lambda\left\|w\right\|^2
$$ 

### 非线性支持向量机  
在线性支持向量机的对偶问题中，目标函数和分类决策函数都只涉及实例与实例之间的内积，不要显示的指定非线性变换,可以用过**核函数来替换其中的内积**。 

#### 核函数 
输入空间$\mathcal X$到特征空间$\mathcal H$的映射$\phi（x:\mathcal X \rightarrow \mathcal H）$,对任意$x,z \in \mathcal X$，有：
$$
K(x,z)=\phi(x)\cdot\phi(z)
$$


构建最优化问题：
$$
\min_\alpha\ \quad \frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N\alpha_i\alpha_jy_iy_jK(x_i,x_j)-\sum_{i=1}^N\alpha_i\\
s.t.\ \ \ \sum_{i=1}^N\alpha_iy_i=0\\
0\leqslant \alpha_i \leqslant C,i=1,2,\dots,N
$$


求解得到$\alpha^*=(\alpha_1^*,\alpha_2^*,\cdots,\alpha_N^*)^T$

选择$\alpha^*$的一个正分量计算
$$
b^*=y_j-\sum_{i=1}^N\alpha_i^*y_iK(x_i,x_j)
$$
构造决策函数
$$
f(x)=sign\left(\sum_{i=1}^N\alpha_i^*y_iK(x,x_i)+b^*\right)
$$