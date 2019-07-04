### 数据库编程

### MYSQL

#### Acknowledgements 
~~[别人总结的太好了，死于完美](https://github.com/jackfrued/Python-100-Days/blob/master/Day36-40/%E5%85%B3%E7%B3%BB%E5%9E%8B%E6%95%B0%E6%8D%AE%E5%BA%93MySQL.md)~~  

#### 创建(删除,选择)数据库 
create database testdb;  
drop database testdb;  
use testdb；#用那个数据库必须切换成相应 

#### 创建（删除）数据表  
create table table_cataglory(catagloryID int(11) not null  auto_increment,catagloryName varchar(50) no ,primary key (catagloryID))ENGINE=InnoDB DEFAULT CHARSET=utf8;   
如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为NULL ，就会报错。 
AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。
PRIMARY KEY关键字用于定义列为主键。 您可以使用多列来定义主键，列间以逗号分隔。
ENGINE 设置存储引擎，CHARSET 设置编码  

drop table table_cataglory; 

desc table_cataglory;
描述表的属性

#### 插入数据  
insert into table_cataglory (catagloryName) values("SAT"),("TOEFL"),("Level 6"),("Level 4"),("GRE");# 一次插入多条数据 

#### 查询数据
select *from table_cataglory;
查询数据表 

#### where 子句
select *from table_cataglory where catagloryName ="Level 4";

#### updata查询
update table_cataglory set catagloryName ="Level 5" where  catagloryID="4";

#### delete 语句
delete from table_cataglory where catagloryName = "Level 5";

#### like子句
select *from table_cataglory where cataglory like "Level%";
SQL LIKE 子句中使用百分号 %字符来表示任意字符

#### union
select catagloryName from table_cataglory union elect catagloryName from tb_cataglory order by catagloryName;
UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中。多个 SELECT 语句会删除重复的数据


### MGONDB
### REDIS
