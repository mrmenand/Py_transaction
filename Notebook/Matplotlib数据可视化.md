## Matplotlib 数据可视化

参考书籍：《Python数据科学手册》
Matplotlib 是建立在NumPy 数组基础上的多平台数据可视化程序库

#### 1.1 导入Matplotlib
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100) ###返回num均匀分布的样本，返回0 到 10 之间100个均匀的样本

#### 1.2 MATLAB风格接口
plt.figure() # 创建图形 
plt.subplot(2, 1, 1)  #创建两个子图中的第一个，设置坐标轴，(行、列、子图编号)
plt.plot(x, np.sin(x))

plt.subplot(2, 1, 2) #创建两个子图中的第二个，设置坐标轴
plt.plot(x, np.cos(x))
plt.show()

#### 1.3 简易线形图
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid') # 创建的图树网格图
import numpy as np
x = np.linspace(0, 10, 100)
fig = plt.figure()
ax = plt.axes()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x)); #一张图中创建多条线
plt.show()

#### 1.3.1 调整图形：线条的颜色与风格

plt.plot(x, np.sin(x - 0), color='blue') # 标准颜色名称
plt.plot(x, np.sin(x - 1), color='g') # 缩写颜色代码（rgbcmyk）
plt.plot(x, np.sin(x - 2), color='0.75') # 范围在0~1的灰度值
plt.plot(x, np.sin(x - 3), color='#FFDD44') # 十六进制（RRGGBB，00~FF）
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB元组，范围在0~1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # HTML颜色名称

plt.plot(x, x + 4, linestyle='-') # 实线
plt.plot(x, x + 5, linestyle='--') # 虚线
plt.plot(x, x + 6, linestyle='-.') # 点划线
plt.plot(x, x + 7, linestyle=':'); # 实点线

#### 1.3.2 调整图形：坐标轴上下限

虽然Matplotlib 会自动为你的图形选择最合适的坐标轴上下限，但是有时自定义坐标轴上下限可能会更好。调整坐标轴上下限最基础的方法是plt.xlim() 和plt.ylim()
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);
另外一个方法是：plt.axis() 方法可以让你用一行代码设置x 和y 的限值
plt.axis([-1, 11, -1.5, 1.5])

#### 1.3.3 设置图形标签

图形标签的方法有：图形标题、坐标轴标题、简易图例
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");

单个坐标轴上显示多条线时，创建图例显示每条线是很有效的方法，plt.legend() 函数会将每条线的标签与其风格、颜色自动匹配

#### 1.4.1 用plt.scatter画散点图

创建一个随机散点图，里面有各种颜色和大小的散点
rng = np.random.RandomState(0)  #跟numpy.random.seed（）一样，是一个伪随机数生成器
x = rng.randn(100) #产生标准正态分布的随机树
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis') #alpha 参数来调整透明，cmp用来映射颜色，viridis为东青色
plt.colorbar(); #显示颜色条

可以用Scikit-Learn 程序库里面的鸢尾花（iris）数据来演示。它里面有三种鸢尾花，每个样本是一种花，其花瓣（petal）与花萼（sepal）的长度与宽度都经过了仔细测量
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T
plt.scatter(features[0], features[1], alpha=0.2,
s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);