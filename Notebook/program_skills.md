 ## Advanced programming skills 

>  2019年6月5日，快要高考了，历尽千帆事，等我学成归来的时候，调整结构，删除没用的，增加应用场景及合适的代码  


### Acknowledgement
[Python高级编程技巧实战](https://coding.imooc.com/class/62.html) 

### 数据结构
#### 1. 如何在列表，字典，集合中筛选数据？
- 列表  data = [randint(-10,10) for _ in range(10)]
    - 过滤器：filter(lambda x: x>0, data)
    - 列表推导：[x for x in data if x>0]

- 字典   data = {x:randint(60,100) for x in range(1,21)}
  - 字典推导： {k:v  for k ,v in data.items if v > 90}

-  集合 data = set([randint(-10,10) for _ in range(10)]) 
   - 集合推导 {x for x in data if x%3 ==0}

#### 2. 如何为元组中的每个元素命名，提高程序可读性 
- 定义类似与其它语言的枚举类型，也就是定义一系列数值常量
                ```
                NAME ,AGE,SEX,EMAIL = range(4)
                student = ("mr_menand",  24 , "male", "1006024749@qq.com") 
                ```
               通过常量访问student[name]

- 使用标准库的collections.namedtuple替代内置tuple 
                ```
                Student = namedtuple("Student",["name", "age","sex","email"])
                s = Student("mr_menand",24,"male","100@qq.com")
                ``` 
                通过类实例化访问, s.name  

#### 3. 如何统计序列中元素出现的频度 
- 字典
   ```
    data = [randint(0,20)  for _ in range(30)]
    c = dict.fromkeys(data,0)
    for x in data:
          c[x] += 1
   ```
-  使用collections.Counter对象 
   - 将序列传入Counter的构造器，得到Counter对象是元素频度  c2 = Counter(data) 
   - Counter(data).most_common(3) 方法得到频度最高的n个元素列表 
   
#### 4. 如何根据字典中值的大小，对字典中的项排序？
- 利用zip将字典元素转换成元组 
  d = {x:randint(60,100) for x in "xyzabc"} 
  sorted(zip(d.values(),d.keys())) 
- 传递sorted函数的key参数  
  sorted(d.items(),key = lambda x : x[1])   

#### 5. 如何快速中找到多个字典中的公共键？
- 遍历
        ```
                s1 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}  
                s2 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}  
                s3 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}  
                res = [] 
                for k in s1:   
                if  k in s2 and k in s3:  
                res.append(k) 
        ``` 
- 利用集合(set)的交集操作 
s1.keys() & s2.keys() & s3.keys()   

#### 6. 如何让字典保持有序？
- 使用collections.OrderedDict  

#### 7. 如何实现用户的历史记录（最多n条）
- 使用容量为n的队列储存历史记录 
- 使用标准库的collections的deque,它是一个双端循环队列 
   q = deque(maxlen=5)  
- 程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入  
   pickle.dump(q.open("history","w"))
   pickle.load(open("history")) 

### 迭代器和生成器 

#### 8. 如何实现可迭代对象和迭代器对象？
l = [randint(0,10) for _ in range(10) ] 
s = "abcdefg" 
l 与 s 是可迭代对象
iter(l) 与 l.__iter__()  都是迭代器对象（__next__）
对于字符串是 s.__getitem__() 生成迭代器对象 

实现一个迭代器对象WeatherIterator，next返回每日天气播报 
实现一个可迭代对象WeatherIterable，__iter__ 方法每次返回一个迭代器对象 
```
from  collections import Iterable,Iterator
import  requests

class  WeatherIterator(Iterator):
        def  __init__(self,cities):
            self.cities = cities
            self.index = 0

        def get_weather_info(self, city_code):
            url = "http://t.weather.sojson.com/api/weather/city/" + city_code
            all_data = requests.get(url).json()

            data = all_data['data']
            forecast = data["forecast"][0]
            ymd = forecast["ymd"]
            week = forecast["week"]
            notice = forecast["notice"]
            type = forecast["type"]
            low = forecast["low"].split()[1]
            high = forecast["high"].split()[1]
            fx = forecast["fx"]

            weather_msg = "小可爱,今天是{ymd},{week}\n {notice} \n 天气:{type} \n 气温:{low}~{high} \n 遇事不决,可问{fx}哦 \n" \
                .format(ymd=ymd, week=week, notice=notice, type=type, low=low, high=high, fx=fx)

            return weather_msg

        def __next__(self):
            if self.index == len(self.cities):
                raise  StopIteration
            city_code = self.cities[self.index]
            self.index += 1
            return  self.get_weather_info(city_code)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def  __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable(["101030100","101020100","101010100"]):
    print(x)
```

#### 9. 如何使用生成器函数实现可迭代对象？
将该类的 __iter__ 方法实现成生成器函数，每次yield 返回一个素数 

生成器对象实现迭代器对象和可迭代对象
```
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False

        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1, 100):
    print(x)
```

#### 10.  如何进行反向迭代以及如何实现反向迭代？
l = [1,2,3,4,5]
l.reverse() 原地反序，打乱顺序 
l[::-1]  生成新的列表，浪费内存 
reversed(l) 生成反向迭代器对象 

实现反向迭代协议的__reversed__ 反法，返回一个反向的迭代器  
```
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x)
```

#### 11.  如何对迭代器做切片操作？
Python中文本文件是可迭代对象  
使用标准库中itertools.islice，它能返回一个迭代对象切片的生成器  
f = open() 
使用islice(f,start,end)生成生成器对象，会消耗原来的对象  
```
l = range(20)
t = iter(l)
for x in islice(t,5,9):
    print(x)
for x in t :
    print(x)
```
####  12. 如何在一个for语句中迭代多个可迭代对象？
 - 并行：使用内置函数的zip，它能将多个可迭代对象合并，每次迭代返回一个元组  
    ```
    for c, m ,e in zip(chinese,math,english):
            total.append(c+m+e)
    ```
 - 串行： 使用标准库的itertools.chain ， 它能将多个可迭代对象连接 
    ```
    for  s in chain(c,m,e):
        if  s > 90 :
             cnt += 1
    ```

### 字符串处理 

#### 13. 如何拆分含有多种分割符的字符串？
- 连续使用str.split()方法，每次处理一种分割符号    
s为字符串，ts为要分割的字符串
  ```
    res = [s]  
    for type in ts:
        t = []
        map(lambda x: t.extend(x.split(type)),res)
        res = t 

   ```
- 使用正则表达式的re.split()方法，一次性拆分字符串  
`re.split(r"[,;\t|]+", s )`

#### 14. 如何判断字符串s是否以字符串a开始或结尾？ 
使用字符串的str.startswith()和str.endswith()方法，注意：多个匹配时使用元组 
`[name for name in os.listdir(".") if name.endswith((".sh",".py"))]`

#### 15. 如何调整字符串中文本的格式 
使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，捕获每个部分内容，在替换字符中调整各个捕获组的顺序  
```
log = open("xx.log").read()
re.sub(r"(\d{4})-(\d{2})-(\d{2})",r"\2/\3/\1,log) 
``` 

#### 16. 如何将多个小字符串拼接成一个大的字符串？
- 迭代列表，连续使用"+"操作依次拼接每一个字符串 
临时字符串，大量的字符串拷贝和对象的释放，字符串很大就很浪费
- 使用str.join()方法，更加快速的拼接列表中的所有字符串 
   生成器表达式比列表推导式更节省内存 
    ```
    l = ["abc",23,556,"xyz"]
    ".join(str(x) for x in l) 
    ```

#### 17. 如何对字符串进行左，右，居中对齐？
- 使用字符串的str.ljust(),str.rjust(),str.center() 进行左右居中对齐 
- 使用format()方法，传递类似"<20"，">20","^"参数完成同样任务  
```
w = max(map(len,d.keys()))
for k in d :
       print(k.ljust(w),":",d[k])
```

#### 18.  如何去掉字符串中不需要的字符？  
- 字符串的strip()，lstrip(), rstrip() 方法去掉字符串两端字符 
- 删除单个固定位置的字符，可以使用切片＋拼接的方式　
- 字符串的replace()方法或正则表达式re.sub()删除任意位置字符串 
  s.replace("\t","")
  re.sub("[\t\r]","",s)
- 字符串translate()方法，可以同时删除多种不同的字符串 

###  文件的I/O操作  

#### 19.  如何读写文本文件 ？
字符串的语言发生了变化  
Python2      Python3 
str      -->     btyes 
unicode    --> str
f  = open('"xx","rt",encoding = "utf-8") 
open函数指定"t"的文本模式，en(d)coding指定编码格式 

#### 20.  如何处理二进制文件？ 
open函数想以二进制打开文件，指定mode参数为"b" 
二进制数据可以用readinto，读入到提前分配好的buffer中，便于数据处理 
解析二进制数据可以使用标准库中的struct模板的unpack方法  
**TODO**

####　21. 如何设置文件的缓冲 ？ 
文件写入操作的I/O操作时间很长，使用缓冲区减少I/O操作次数  
Python中文件对象默认缓冲区大小为4096 
- 全缓冲 ，open函数的buffering设置为大于1的整数n，n为缓冲区大小 
- 行缓冲（ttf,shell终端设备)，open函数的buffering设置为1 
- 无缓冲（串口）,open函数的buffering设置为0  

####  22. 如何将文件映射到内存？
使用标准库中的mmap模板的mmap()函数，它需要一个打开的文件描述符作为参数 
 1. 访问某些二进制文件中时，希望把文件映射到内存，可以实现随机访问 
 2. 某些嵌入式设备，寄存器被编址到内存地址空间  
 3. 如果多个进程映射同一个文件，实现进程通信的目的  
 **TODO** 

#### 23. 如何访问文件的状态？ 
- 需要获得文件状态：
   - 文件的类型（普通文件，目录，符号链接，设备文件···）
   - 文件的访问权限 
   - 文件的最后访问/修改/节点状态更改时间 
   - 普通文件的大小 

-  标准库中os模板下的三个系统调用stat,fstat,lstat 获取文件状态  
   - os.stat() 获取的文件状态信息  
    **TODO每个状态怎么表示的?**  
   - os.lstat() 获取的是符号文件状态  
   - os.fstat() 类似文件stat,需要文件描述符f.fileno() 
- 标准库中os.path下的一些函数，使用起来更加简洁 

####  24.  如何使用临时文件？ 
- 临时文件不用命名，且关闭后会自动被删除 
采集数据做分析，最终只保存分析结果，用临时文件（慎）  
- 使用标准库的tempfile下的TemporaryFile，NameTemporaryFile   

### 数据编码与处理  

#### 25. 如何读取csv数据？
使用标准库的csv模板，可以使用其中的reader和writer完成csv文件读写 
```
    with open("piangan.csv","rb") as rf:
        reader = csv.reader(rf)
        with open("pingan2.csv","wb") as wf:
            writer  = csv.writer(wf)
            header = reader.next()
            writer.writerow(header)
            for row in reader:
                if row[0] < "2016-01-01":
                    break
                if int(row[5]) >= 50000000:
                    writer.writerow(row)  
 ```

 #### 26.  如何读写json数据 
 JSON(JavaScript Obeject Notation) 是一种轻量级的数据交换格式 
 - 使用标准库的json模板，其中load,dump函数可以完成json文件的读取 
   - load，dump读取的是数据对象 
   - loads, dumps读取的是文件对象  

####  27.   如何解析简单的xml文件  
XML 指可扩展标记语言（eXtensible Markup Language）  
- 使用标准库中的xml.etree.ElementTree,其中的parse函数可以解析xml文档 
TODO：

#### 28.  如何构建xml文档
- 使用标准库中的xml.etree.ElementTree，构建ElementTree，使用write方法写入文件  
TODO：


#### 29. 如何读写excel文件 
- 使用第三方库xlrd和xlwt,这两个库分别用于excel读和写  
TODO：感觉很鸡肋，应用场景？

###  类与对象 

####  30. 如何派生内置不可变类型并修改实例化行为？ 
- 定义类IntTuple继承内置tuple, 并实现__new__，修改实例化行为  
 __new__在__init__之前执行  
    ```
        def __new__(cls, iterable):
            g = (x for x in iterable if isinstance(x, int) and x > 0)
            return super(IntTuple, cls).__new__(cls,g)
    ```

####  31. 如何为创建大量实例节省内存？ 
- 定义类的__slots__属性，它是用来声明实例属性名字的列表，类似C语言的结构体 
动态绑定属性的特性绑定内存做代价，主要体现在sys.getsizeof（p.__dict__)上 

####  32 如何让对象支持上下文管理 ？ 
- 实现上下文管理协议，需要定义实例的__enter__，__exit__方法，它们分别在with开始和结束时被调用 
TODO: 实现自己的

#### 33. 如何创建可管理的对象属性？  
- 使用property函数为类创建可管理属性 
- 使用@property装饰器 

#### 34. 如何让类支持比较操作？ 
- 比较符号运算重载，需要实现以下方法：
__lt__,__le__,__gt__,__ge__,__eq__,__ne__    
    ```
        def __lt__(self, obj):
            print("in__lt__")
            return self.area() < obj.area()

        def __le__(self, obj):
            print("in__le__")
            return self.area() <= obj.area()  
    ```
- 使用标准库下的functools的类装饰器total_ordering可以简化此过程 
  只需需要定义至少一种方法,就可以推导出 


#### 35. 如何使用描述符对实例属性做类型检查  
- 可以对实例变量名指定类型 ，赋予不正确类型时抛出异常 
- 使用描述符来实现需要类型检查的属性 
分别实现__get__,__set__,__delete__方法，__set__内使用isinstance函数做类型检查
  ```
      def __set__(self, instance, value):
        if not instance(value,self.type_):
            raise TypeError("expected an %s "%self.type_)
        instance.__dict__[self.name] = value
  ```

#### 36. 如何在环状数据结构中管理内存？   
在Python中,垃圾回收器通过引用技术来回收垃圾对象的，但某些环状数据结构（树、图···）,存在对象间的循环引用。
- 使用标准库weakref，它可以创建一种能访问对象但不增加计数的对象 
TODO

#### 37. 如何通过实例方法名字的字符串调用方法？
- 使用内置函数getattr，通过名字在实例上获取方法对象，然后调用 
   ```
   def getArea(shape):
         for name in ("area","getArea","get_area"):
                f = getattr(shape,name,None)
                if  f:
                    return f()
   ```
- 使用标准库operator下methodcaller函数调用 
  实际情况感觉没用 

###  多线程和多进程

#### 38.  如何使用多线程？
Threading
- TODO 自己总结 

####  39. 如何线程间通信？ 
 由于全局解释锁GIL的存在，多线程进行CPU密集型操作并不能提高执行效率 
- 使用多个DownloadThread线程进行下载(I/O操作) 
- 使用一个ConvertThread线程进行转换（CPU密集型操作） 
-  使用标准库的Queue.Queue，它是一个线程安全的队列，Download线程把下载数据放入队列，Convert线程从队列里提取数据 
TODO：线程与异步aiohttp 

####  40. 如何在线程间进行时间通知？
线程间的事件通知，可以使用标准库中Threading.Event 
等待事件一端调用wait,等待事件 
通知事件一端调用set ,通知事件  
TODO

#### 41.  如何使用线程本地数据 
threading.local函数可以创建本地数据空间，其下属性对每个线程独立存在  
TODO


#### 42. 如何使用线程池？
对请求连接数做限制，使用线程池，替代原来的每次请求创建线程 
TODO 

#### 43.如何使用多进程？ 
- 由于Python中全局解释器锁GIL的存在，在任意时刻只允许一个线程在解释器中运行。因此Python的多线程不适合处理cpu密集型的任务.
想要处理cpu密集型的任务，可以使用多进程模型 
- 使用标准库的multiprocessing.Process，它可以启动子进程执行任务，操作接口，进程间通信，进程间同步等都与Threading.Thread类似 
- 通过Queue和pipe进行进程间的通信 

### 装饰器 

#### 44.如何使用函数装饰器？
定义装饰器函数，用它来生成一个原函数添加了新功能的函数，替代原函数 
  ```
  def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(50))

  ```


####  45. 如何为被装饰的函数保存元数据 
在函数对象中保存着一些函数的元数据，使用装饰器后，属性访问后看到是内部包裹的元数据，原来函数的元数据丢失 
- 使用标准库functools中的装饰器wraps装饰内部包裹函数，可以定制将原函数的某些属性，更新到包裹函数上去 
@wraps(func)

#### 46. 如何定义带参数的装饰器  
实现一个装饰器，用来检查被装饰函数的参数类型，装饰器可以通过参数指明函数参数的类型，调用时如果检测出类型不匹配则抛出异常。 
- 生产装饰器的工厂，inspect.signature()方法，每次调用typeassert，返回一个特定的装饰器，然后去用它修饰其他函数 
TODO

#### 47. 如何实现属性可修改的函数装饰器 
为包裹函数增添一个函数，用来修改闭包中使用的自由变量 
使用弄nonlocal访问嵌套作用域中的变量引用 
```
def warn(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            used = time.time() - start
            if used > timeout:
                msg = f"{func.__name__}:{used}> {timeout}"
                logging.warn(msg)
            return res

        def setTimeout(k):
            nonlocal timeout
            timeout = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator
```



 











