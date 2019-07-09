### Django 
[Django中文文档](https://docs.djangoproject.com/zh-hans/2.1/)

Django框架遵循MVC设计，并且有一个专有名词：MVT 

- MVT 
  - M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理。
  - V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。
  -  T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html 


 #### 模型 

-  ORM 
    -  O(objects):类和对象。 R(Relation):关系，关系数据库中的表格。M(Mapping):映射
   - Django ORM框架的功能：
     - 实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，而不需要修改代码。
     - 只需要面向对象编程，不需要面向数据库编写代码。
     - 在MVC中Model中定义的类，通过ORM与关系型数据库中的表对应，对象的属性体现对象间的关系，这种关系也被映射到数据表中。

- 定义属性和字段类型及选项 
- 条件查询 
   - 字段查询 
   实现sql中where的功能，调用过滤器filter()、exclude()、get()  
   通过"属性名_id"表示外键对应对象的id值  

   - 条件查询符 
     - exact：表示判等 
     - contains：是否包含 
     startswith、endswith：以指定值开头或结尾  
     -  isnull：是否为null 
     - in：是否包含在范围内 
     - gt、gte、lt、lte：大于、大于等于、小于、小于等于
     - year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算 
  
  - F对象 
  之前的查询都是对象的属性与常量值比较，两个属性怎么比较呢？
  答：使用F对象（），被定义在django.db.models中 
  F(属性名) 
  - Q对象 
  多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字 
  Q(属性名__运算符=值) 
  Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或 

  - 聚合函数 
  使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg，Count，Max，Min，Sum，被定义在django.db.models中   

- 查询集  
   - 查询集可以含有零个、一个或多个过滤器。过滤器基于所给的参数限制查询的结果，从Sql的角度，查询集和select语句等价，过滤器像where和limit子句。
   - 可以对查询集进行取下标或切片操作，等同于sql中的limit和offset子句 

- 关联  
   - 关系字段类型 
      - ForeignKey：一对多，将字段定义在多的一端中。
      - ManyToManyField：多对多，将字段定义在任意一端中。
      - OneToOneField：一对一，将字段定义在任意一端中。
      -  可以维护递归的关联关系，使用'self'指定，详见"自关联"。 

  - 关联查询  
    - 通过对象执行关联查询 
       - 一到多的访问语法 ： 一对应的模型类对象.多对应的模型类名小写_set 
       -  由多到一的访问语法: 多对应的模型类对象.多对应的模型类中的关系类属性名 
    - 通过模型执行关联查询 
     关联模型类名小写__属性名__条件运算符=值  

  - 自关联 
  内部的关系字段指向本表的主键，这就是自关联的表结构 
  aParent=models.ForeignKey('self',null=True,blank=True)#关系 

- 模型类扩展 
  - 模型实例方法：delete()、save() 
  - 模型类的属性：属性objects：管理器，是models.Manager类型的对象，用于与数据库进行交互  
  - 管理器Manager 
     -  管理器是Django的模型进行数据库操作的接口，Django应用的每个模型类都拥有至少一个管理器。Django支持自定义管理器类，继承自models.Manager。
    - 自定义管理器类主要用于两种情况：
        1.修改原始查询集，重写all()方法
        2.向管理器类中添加额外的方法，如向数据库中插入数据。
  - 元选项 
  在模型类中定义类Meta，用于设置元信息，如使用db_table自定义表的名字。 
  `   class Meta:db_table='bookinfo' #指定BookInfo生成的数据表名为bookinfo`


####  视图 
- URFconf  
- 视图 
- HttpRequest对象 
- HttpResponse对象 
- 状态保持 


#### 模板  

- 模板语言 
- 模板继承 
- HTML转义  
- CSRF  
- 验证码  
- 反向解析  

#### 常用 

- 静态文件的处理 
- 中间件 
- Admin站点 
- 上传图片 
- 分页 