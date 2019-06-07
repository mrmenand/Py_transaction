## Effective Python 编写高质量Python代码的59个有效方法 

> 始于2019年6月3日， 剧终前补完每条的代码 

### Acknowledgement 
[59个编写高质量Python代码的中文翻译版](https://guoruibiao.gitbooks.io/effective-python/content/)   暴躁老哥翻译的巨坑 而且没翻译完 

### Pythonic Thinking 
Python之禅：`import this` 
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough  to break the rules 

#### 1. 了解你正在使用的Python版本 
- 查询正在使用的版本：
`python --version`  
- Python有用多个运行时环境：CPython，Jython,IronPython,PyPy
- 自带和Anaconda都是默认Cpython解释器，PyPy(使用Just-in-Time(JIT)即时编译器，即动态编译器)比Cpython快

#### 2. 遵循PEP 8风格编程风格 
写代码的时候总是要遵循PEP 8的风格指导  
pycharm开发环境可以通过安装  
`pip install autopep8`包,自动调整为pep8编码风格，详情自己百度 

#### 3. 了解字节，字符串以及unicode之间的区别 
python3x 中：
 - 有两种类型的字符代表序列：bytes(字节)和 str（字符串）  
- str 在内存中的编码方式是unicode 
- str不能直接存储，和发送   

```
s = "mr_menand" 
a = "向维维"
s1 = s.encode("utf-8") # 将unicode --> utf-8编码，是bytes类型 
s2 = a.encode("utf-8)" # 输出为：b'\xe5\x90\x91\xe7\xbb\xb4\xe7\xbb\xb4'  
``` 
TODO：反射，编码规范

#### 4. 用辅助函数来取代复杂表达式  
 - 在Python中，空字符串，空列表，零值等都可以被隐式的转换为False值，接下来的表达式中的子表达式为False的时候就会自动的被替换为or 运算符后面的子表达式   
 - 布尔表达式（or 或者 in ）的一个更好的替代方案就是使用if/else，来增强代码的可读性  

 ####  5. 了解切割序列的方法  
 Python中的常用序列：str字符串，list列表，bytes字节 
对于实现了__getitem__和__setitem__这两个特殊方法的类都可以使用分片机制   

####  6.  在单次切片操作中，不要同时指定start、end 和 stride  
- 步幅Bug:当数据仅仅为ASCII码内数据时工作正常,出现Unicode字符的时候就会报错  
- 在分片中指定start，end,stride会让人感到困惑，难于阅读 
- 先分片再调幅  
 - 内置模块中的迭代器itertools的islice方法 

#### 7.  用列表推导式取代map和filter 
- 列表表达比内置的map,filter更加清晰，而且更快 
- 字典和集合也都支持列表表达式，没有元组推导式 

#### 8.  在列表表达式中避免使用超过两个的表达式  
- 表达式运行的顺序是由左至右  
- 列表表达式支持多层的循环和条件语句，以及每层循环内部的条件语句 
-  多个表达式并不正常循环体简洁 

#### 9.  用生成器表达式来改写数据量较大的列表推导 
- 列表表达式的缺点：
存在列表的拷贝和对象的释放，不好处理数据量较大的序列  
- 生成器表达式的好处： 
  - 生成一个generator迭代器,防止内存危机 
     生成器表达式通过使用类似于列表表达式的语法（在()之间而不是[]之间，仅此区别）来创建 通过迭代的方式来处理每一个列表项
  -  链式操作
     `roots = ((x,x**0.5) for x in it)` 
-  通过生成器表达式返回的迭代器是有状态的 

#### 10.  尽量使用enumerate取代range 
- Python提供了一个枚举函数enumerate,可以使用懒模式来包装任何的迭代器 。
- 遍历迭代器同时既能获取下标，也能获取当前值
- 尽量用enumerate改写将range与下标访问相结合的序列遍历代码 
- 可以添加第二个参数来指定索引开始的序号，默认为0
  

#### 11. 用zip函数同时遍历两个迭代器 
- zip相当于生成器，会在遍历的过程逐次产生元组 
- 如果迭代器长度不等，自动提前啊终止 
- itertools 的zip_longgest不用在乎长度 

##### 12. 不要在for和while循环后面写else块 
- Python有用特殊的语法，可在for及while循环体结束后立即执行 
- 只有当整个循环主题都没有遇到break语法时，循环后面的else块才会执行 
- 避免在循环体的后面使用else语块，因为这样的表达不直观，而且容易误导读者  

####  13. 合理利用try/except/else/finally结构中的每个代码块 
- try读取文件并处理其内容
- except块对应try块中可能发生的相关异常 
- else块实时地更新文件并把更新中可能出现的异常回报给上级代码， 可以最大限度的减少try块中的代码的长度，并且可以可视化地辨别try/except成功运行的部分。
- finally块清理文件句柄 

### Function函数 

#### 14. 尽量用异常来表示特殊情况，而不要返回None  

None和其他的变量（例如 zero，空字符串），在条件表达式判断中是等价的（False） 
个人习惯：return -1

#### 15.  了解如何在闭包（closure）里使用外围作用域中的变量 

- Python支持闭包：可以引用声明域比自己高的变量，从变量被定义的作用域内引用变量
    - Python搜索变量的LEGB顺序（Local --> Embedded --> Global --> Built-in）
    -  声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）。 
    - nonlocal：声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）。
- Python的函数是一等对象（first-clas-object）, 函数可以作为参数传递 
-  在Python3中，可以使用nonlocal自由标记关键字来突破闭包的限制，进而在其检索域内改变其值，尽量避免使用 

TODO这书讲的不准 

#### 16. 考虑用生成器来改写直接返回列表的函数  
   ```
   def index_words_iter(text):
   if text:
         yield 0
   for index, letter in enumerate(text):
         if letter ==" ":
            yield index + 1
   ```
   - 相较于返回一个列表的情况，替代方案中使用生成器可以使得代码变得更加的清晰 
   - 生成器可以处理很大的输出序列就是因为它在处理的时候不会完全的包含所有的数据  


#### 17. 在参数上面迭代的时候，要多加小心  
迭代器是状态相关的，并且不能被重用 

####  18. 用数量可变的位置参数减少视觉杂讯 
令函数接受可选择位置参数 *atgs，减少视觉杂讯（visual noise） 
- 可变参数在被传递给函数的时候进程会被转变成元组 
-  新增位置参数时，存在函数移植问题 

#### 19. 用关键字参数来表示可选的行为  
- ，函数参数可以按位置或和关键字来指定，可读性提高 
- 初始化一个默认值，提供一个很好的拓展功能 
-  可选参数做到向后兼容   


#### 20. 用None和文档字符串来描述具有动态默认值的参数 
默认参数只会被赋值一次 
如何参数的实际默认值是可变类型（mutable）,务必用None作为形式  


#### 21. 用只能以关键字形式指定的参数来确保代码明晰 
适用keyword-only参数可以强迫函数调用者提供关键字来赋值，这样对于容易使人疑惑的函数参数很有效，尤其适用于接收多个布尔变量的情况  

### 类与继承 

#### 22. 尽量使用辅助类来维护程序的状态，而不要使用用字典和元组 
 - 字典类型维护动态内部状态维护非常好用，字典的多级嵌套，代码变得难于阅读，难于维护 
 - namedtuple具名元组  
 -  当内部的字典关系变得复杂的时候将代码重构到多个工具类中


#### 23. 简单的接口应该接受函数，而不是类的实例 
- Python中的许多内置的API都允许你通过向函数传递参数来自定义行为。这些被API使用的hooks将会在它们运行的时候回调给你的代码 
- Python中引用函数和方法的原因就在于它们是first-class，可以直接的被运用在表达式中  
- 特殊方法__call__允许你像调用函数一样调用一个对象实例  

#### 24.  使用@classmethod多态性构造对象 
类方法（不需要实例化类就可以被类本身调用） 
TODO 没搞懂classmethod与多态的关系 

#### 25. 用super初始化父类 
Python采用标准的方法解析顺序来解决超类初始化次序及钻石继承问题 
super 函数定义了解析顺序（method resolution order）（深度优先，从左到右） 
总是使用内置的super函数来初始化父类 

####  26. 只有使用Mix-in 组件制作工具类时进行多重继承 
TODO 没明白 

####  27. 多用public属性，少用private属性 
- Python编译器无法严格的保证private字段的私密性 
- 多用protected属性，在文档中把这些字段的合理用法告诉子类的开发者，而不要试图用private属性来限制子类访问这些字段 


#### 28. 继承 collections.abc以实现自定义的容器类型 

编写自制的容器类型时，可以从collections.abc 模块的抽象基类中继承，确保子类具备适当的接口及行为。 

### 元类（metaclass）及属性  
TODO：讲的这么多都不太理解，自己总结合适的 

#### 29. 用纯属性取代get和set方法 
- 编写新类时，应该用简单的public属性来定义其接口，而不是手工实现set和get方法 
- 如果访问对象的某个属性时，需要表现特殊行为，那就用@property装饰

#### 30. 考虑用@property来代替属性重构 
- @property 可以为现有的实例属性添加新功能 

#### 31. 用描述符来改写需要复用的@property方法 


#### 32. 用__getattr__和__setattr__实现按需生成的属性 
- 通过__getattr__和__setattr__，我们可以用惰性的方式来加载并保存对象的属性 
- 理解__getattribute__和__getattr__的区别：前者在待访问的属性缺失时出发，而后者每次访问都触发  

#### 33. 用元类来验证子类 
通过元类的__new__方法，可以在生成子类对象之前，先验证子类的定义是否合乎规范 

#### 34. 用元类来注册子类 
类的继承

#### 35. 用元类来注解类的属性 


###  并发（concurrency）与并行(parallelism)  
并发，计算机（seemingly）在同一时间做着不同的事 
并行，计算机（actually）在同一时间做着不同的事 
区别：提速（speedup）

####  36.  用subprocess 模板来管理子进程 

####  37. 可以用线程来执行阻塞式的I/O，但不要它做平行计算  

#### 38. 线程中使用Lock 来防止数据竞争 

#### 39. 用Queue来协调各线程之间的工作 

#### 40. 考虑用协程来并发地运行多个函数 

#### 41. 考虑用concurrent.future来实现真正的并行计算 

### 内置模板 

#### 42. 用functolls.warps定义函数修饰器 

#### 43. 考虑以contextlib 和with语句来改写可复用的try/finally代码 

#### 44. 用copyreg实现可靠的pickle操作 

#### 45. 应用datetime模块来处理本地时间，而不是tim模板 

#### 46. 使用内置的算法与数据结构 

#### 47. 在重视精确度的场合，应该使用decimal 

#### 48. 学会安装由Python开发者社区所构建的模块 

### 协作开发  

#### 49. 为每个函数、类和模块编写文档字符串 

#### 50.  用包来安排模块，并提供稳固的API 

#### 51. 为自编的模块定义根异常，以便将调用者和API相隔离 

#### 52. 用适当的方式打破依赖关系 

#### 53. 用虚拟环境隔离项目，并重建依赖关系  

### 部署 

#### 54.  考虑用模块级别的代码配置不同的部署环境 

#### 55. 通过repr字符串来输出调试信息 

#### 56.  用Unittest来测试全部代码  

#### 57. 考虑用pdb实现交互测试  

#### 58. 先分析性能，然后再优化  

#### 59.  用tracemalloc 来掌握内存的使用和泄露情况 