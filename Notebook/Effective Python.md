## Effective Python 编写高质量Python代码的59个有效方法 

### Acknowledgement 
[59个编写高质量Python代码的中文翻译版](https://guoruibiao.gitbooks.io/effective-python/content/) 标题翻译的我想打人，看这个请具备认知性       



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
  

