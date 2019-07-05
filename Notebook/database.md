### 数据库编程

### MYSQL

#### Acknowledgements 
~~[别人总结的太好了，死于完美](https://github.com/jackfrued/Python-100-Days/blob/master/Day36-40/%E5%85%B3%E7%B3%BB%E5%9E%8B%E6%95%B0%E6%8D%AE%E5%BA%93MySQL.md)~~  


### NOSQL 
一类新出现的数据库(not only sql)，它的特点: 
- 不支持SQL语法
- 存储结构跟传统关系型数据库中的那种关系表完全不同，nosql中存储的数据都是KV形式
- NoSQL的世界中没有一种通用的语言，每种nosql数据库都有自己的api和语法，以及擅长的业务场景
- NoSQL中的产品种类相当多：
  - Mongodb
  - Redis
  - Hbase hadoop
  - Cassandra hadoop
- 事务”特性的支持：sql对事务的支持非常完善，而nosql基本不支持事务

### MongoDB 
- MongoDB 是一个面向文档存储的数据库 

### REDIS
Redis 是一个高性能的key-value数据库 
- Redis特性 
  - Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
  -  Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
  -  Redis支持数据的备份，即master-slave模式的数据备份。

- redis应用场景
  - 用来做缓存(ehcache/memcached)——redis的所有数据是放在内存中的（内存数据库）
  - 可以在某些特定应用场景下替代传统数据库——比如社交类的应用
  - 在一些大型系统中，巧妙地实现一些特定的功能：session共享、购物车 

- 数据结构：
redis是key-value的数据结构，每条数据都是一个键值对 
键的类型是字符串 
值的类型分为五种：
  - 字符串string
  - 哈希hash
  - 列表list
  - 集合set
  - 有序集合zset  

- 数据操作 
  - 详细看官方文档 （课程资料）

- 主从概念 
  - 一个master可以拥有多个slave，一个slave可以拥有多个slave，如此下去，形成了强大的多级服务器集群架构
  -  master用来写数据，slave用来读数据，经统计：网站的读写比率是10:1
  - 通过主从配置可以实现读写分离 


- 集群 
  - 集群是一组相互独立的、通过高速网络互联的计算机，它们构成了一个组，并以单一系统的模式加以管理。一个客户与集群相互作用时，集群像是一个独立的服务器。集群配置是用于提高可用性和可缩放性  
  - Redis集群 
    - 软件层面：只有一台电脑，在这一台电脑上启动了多个redis服务 
    - 硬件层面：存在多台实体的电脑，每台电脑上都启动了一个redis或者多个redis服务 
