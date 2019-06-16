#### 1. __repr__  和 __str__ （包含repr）是把一个对象用字符串的形式表达出来 ，增加可读性

#### 2. 列表推导同filter和map的比较
symbols= '$¢£¥€¤'
- 列表推导：`beyond_ascii = [ord(s) for s in symbols if ord(s) > 127] `  
- map/filter：`list(filter(lambda c: c > 127, map(ord, symbols)))`  

#### 3.  生成器表达式 
生成器表达式背后遵守了迭代器协
议，可以逐个地产出元素，节省内存 
- 列表推导式：`tshirts = [(color, size) for color in colors for size in sizes]`
- 生成器表达式：`for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):`


#### 4.  元组拆包 Unpacking 
- 平行赋值  
- *运算符把一个可迭代对象拆开作为函数的参数 
- *在平行赋值中返回的是一个列表`a, b, *rest = range(5)` 
- -占位符忽略不感兴趣的数据 
- 嵌套元组拆包 

#### 5.  具名元组nametuple 
collections.namedtuple 是一个工厂函数，它可以用来构建一个带
字段名的元组和一个有名字的类  
```
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
```
通过字段名或者位置访问 

#### 6. 对序列使用+和*
序列（有序，支持切片，如列表、元组、字符串等）默认是支持+和*操作的
通常 + 号两侧的序列由相同类型的数据所构成，在拼接的过程中，两个被操作的序列都不会被修改，Python 会新建一个包含同样类型数据的序列来作为拼接的结果 
> collections.ChainMap 可以对几个字典进行重映射 

 #### 7.  用bisert来管理已排序的序列
 bisert模板包含两个主要函数，bisect 和 insort，两个函数都利用二分查找算法来在有序序列中查找或插入元素  
> 尾部添加数据，再排序的复杂度是O(nlogn),二分查找只需要O(logn)，在数据量规模很大，时间会很慢  
list.sort()是原地排序，sorted()会新建一个数组，通过key和lamda表达式进行选择性排序 

#### 8. 字典映射
- 字典推导
- dict
d.get(k, default)给找不到键一个默认的返回值
d.setdefault()处理找不到的键,参数(key, value)的可迭代对象或者关键字参数 
d.update(dict)插入新值或者更新已有键值对 
- collections.defaultdict
处理找不到的键  
- collections.OrderedDict
建立有序字典
- dict和set的背后的散列表,详情看[散列表算法法]()部分

#### 9.  闭包 
只有涉及嵌套函数时才有闭包问题  
内部函数包含对外部作用域的变量引用，变量必须是非全局作用域（自由变量的绑定）
类的实例是可调用对象  
nonlocal声明把变量标记为自由变量（函数中为变量赋予新值，也会变成自由变量）

#### 10. 装饰器
```
@d
fun1()
```
等价于fun1 = d(fun1)
```
@d1
@d2
fun1
```
等价于fun1 = d1(d2(fun1))
- property 
 @property --> func 将方法伪装成属性 
 @func.setter --> func 对伪装的属性进行赋值的时候调用这个方法 一般情况下用来做修改 
 @func.deleter --> func 在执行del 对象.func的时候调用这个方法 一般情况下用来做删除 
 - classmethod 
 @classmethod,类方法，使用类中的静态属性  
- @staticmethods
@staticmethods,静态方法,既不使用对象的属性也不使用类中的静态属性时

#### 11. 私有属性和保护属性 
（1）_xxx      "单下划线 " 开始的成员变量叫做保护变量，意思是只有类实例和子类实例能访问到这些变量，
需通过类提供的接口进行访问；不能用'from module import *'导入
（2）__xxx 类中的私有变量/方法名 （Python的函数也是对象，所以成员方法称为成员变量也行得通。）,
" 双下划线 " 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
（3）__xxx__ 系统定义名字，前后均有一个“双下划线” 代表python里特殊方法专用的标识，如 __init__（）代表类的构造函数

#### 12. == 和 is 的区别 
 == 比较的是数值， is 比较的是内存地址 
 * 数据类型为字符串时，只要两个变量赋相同的内容，两个变量为同一对象；
 * 数据类型为元组、列表、字典时。即使两个变量赋相同的内容，也不是同一对象；
 * 数据类型为数值时，两个变量赋相同值，不一定是同一对象。 

#### 13. 内置方法 
- __len__ len(obj)的结果依赖于obj.__len__()的结果，计算对象的长度
- __hash__ hash(obj)的结果依赖于obj.__hash__()的结果，计算对象的hash值
 - __eq__ obj1 == obj2 的结果依赖于obj.__eq__()的结果,用来判断值相等 
 - __str__ str(obj) print(obj) '%s'%obj 的结果依赖于__str__,用来做输出、显示 
 - __format__ format() 的结果依赖于__format__的结果，是对象格式化的 
 - __call__ obj()相当于调用__call__，实现了__call__的对象是callable的 
 - __new__ 构造方法，在执行__init__之前执行，负责创建一个对象，在单例模式中有具体的应用 
- __del__  析构方法，在对象删除的时候，删除这个对象之前执行，主要用来关闭在对象中打开的系统的资源  

#### 14. colltections库 
 - namedtuple: 生成可以使用名字来访问元素内容的tuple 
 - deque: 双端队列，可以快速的从另外一侧追加和推出对象  
- Counter: 计数器，主要用来计数 
- OrderedDict: 有序字典 
- defaultdict: 带有默认值的字典  

#### 15. 反射 
使用字符串数据类型的变量名来使用变量 
1. 文件中存储的都是字符串 
2. 网络上能传递的也最接近字符串  
3. 用户输入的也是字符串 


#### 99. 踩坑录 
1. 字符串“23.1”不能转化成整型，其中只能包括数字 
2. 不要在循环里调用方法，不然就是每一次都调用，如set(B),时间复杂度会乘上set()方案的时间，耗时剧增 
3. **set集合**是一个无序的不重复元素序列，可以做 **-**  求差 、**|** 并集 、**&** 交集 、**^** 不同时包含a,b的元素 

