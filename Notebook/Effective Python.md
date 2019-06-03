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

####  6. 在单次切片操作中，不要同时指定start、end 和 stride 
- 步幅Bug:当数据仅仅为ASCII码内数据时工作正常,出现Unicode字符的时候就会报错  
- 在分片中指定start，end,stride会让人感到困惑，难于阅读 
  - 先分片再调幅  
  - 内置模块中的迭代器itertools的islice方法 


