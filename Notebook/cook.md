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












