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
$$
w^*\cdot x+b^*=0
$$
相应的分类决策函数 
$$
f(x)=sign(w^*\cdot x+b^*)
$$ 

#### 学习的对偶算法 
$$
L(w,b,\alpha) = \frac{1}{2}w\cdot w-\left[\sum_{i=1}^N\alpha_i[y_i(w\cdot x_i+b)-1]\right]\\
&=\frac{1}{2}\left\|w\right\|^2-\left[\sum_{i=1}^N\alpha_i[y_i(w\cdot x_i+b)-1]\right]\\
&=\frac{1}{2}\left\|w\right\|^2-\sum_{i=1}^N\alpha_iy_i(w\cdot x_i+b)+\sum_{i=1}^N\alpha_i
$$