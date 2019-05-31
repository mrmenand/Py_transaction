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


