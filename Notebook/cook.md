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

