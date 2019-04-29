<p align="center"><img width="256px" src="./res/xiuxian.jpg"></p>

[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![Badge](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu/#/zh_CN)
[![HitCount](http://hits.dwyl.io/mrmenand/mrmenand/Py_transaction.svg)](http://hits.dwyl.io/mrmenand/mrmenand/Py_transaction)

> 我亦成仙，快乐修仙！

## LeetCode修仙彔
* LeetCode 刷题笔记
* 人生苦短，我用Python成仙
* 你看这个Python耗时又长，内存又宽，但是TM（提莫）简洁呀，欢迎来Battle
* 学习更加pythonic的写法


## Question Type

- Array
- String
- Linked List
- Stack
- Heap
- Tree
- Hash Table
- Math
- Two Pointer
- Sort
- Binary Search
- Dynamic Programming
- Greedy

## Acknowledgments

- [LeetCode 中国](https://leetcode-cn.com/)

## 日彔
4.23 刷题后开始写笔记 
* 605 种花问题
防御式编程思想，防止漏掉边界情况，在边界两段加0
种花问题可以遍历数组是否有三个连续的0

* 665 非递减数列
转变成数组是否只有一个凹点 
如果i-2的节点小于i,则i-1 指向 i，反之，i 指向i-1

* 709 转换成小写字母
ord A-Z的ASCII码为65-90，ord a-z 为97-122

* 804 唯一摩尔斯密码
如何快速把两个列表合成一个字典
`morse_code = dict(zip([chr(i) for i in range(97,132)],morse))`

4.24 
* 657 机器人能否返回原点
返回左右，上下移动的次数是否一致 用字典建立坐标系更有通用性dict={R:[0,1]},到多维

* 929 独特的电子邮件地址
根据@分割email，分割+，选取作为0，替换"."为空 字符串的拼接

* 344 反转字符串
根据字符串中心反转，交换i,len(s)-1-i的位置

* 13 罗马数字的转换
用字典建立HashMap,遍历当前i，比后面大加上字典value,反之减去，加上边界len(s)的值

4.25 
* 824 山羊拉丁文
对分割后列表中的字符串用索引进行判断，交换首末位置`word[i][1:] + word[i][:1]`,`" ".join(List)`列表联合，不需要推导式

* 788 旋转数字
把i转化成字符串，判断`'3','4','7'，continue,'2','5','6','9',cnt +=1 `是否在字符中，不需要使用列表，减少内存

* 937 重新排列日子文件
判断最后以为`isdigit()`建立两个列表，然后字符排序，`str_log.sort(key = lambda x: x.split()[1:])`,最后字符串拼接

4.26 
* 38 报数
s指向上一轮的报数情况，遍历len(s),`j < len(s)-1 and s[j] == s[j+1]`进行判断length是否有加，反之，拼接字符串，length置0

* 67 二进制求和
`bin(int(a,2)+int(b,2))[2:]`int()默认十进制，带参数的进制，a,b需要以字符串形式输入
相应的还有oct()和hex（）函数

* 551 学生出勤记录I
统计A,超过1则返回假，遍历判断`if i < len(s)-2 and s[i] == s[i+1] == s[i+2] == "L":`

4.27
* 345 反转字符串中的元音字母
双指针，都在元音中，则交换位置，不在则移动指针

* 541 反转字符串
前k个反转，后k个不反转，以2k为间隔`for i in range(0,len(s),2*k),res+=s[i:i+k][::-1]+s[i+k:i+2*k]`

4.28
* 415 字符串相加
用eval（）函数执行一个字符串表达式`str(eval(num1+"+"+num2))`

* 925 长键按入
用时最短的代码简直骚断了腿，只有相等时，i才加`if name[i]==typed[j]:i+=1`，每次遍历都j+=1，最后判断是`i==len(name)`

* 459 重复的子字符串
可以在（1，len(s)//2+1）遍历，`if s[i] == s[0] and s[:i] * (len(s)//i) == s` 判断重复的开始的位置以及复制相应倍数

* 125 验证回文串
用过滤函数filter,返回的是一个可迭代对象，function函数为用的是str.isalnum???为什么没有括号`s = "".join(filter(str.isalnum, s)).lower()`，然后切片判断s == s[::-1]

* 28 实现strStr()
`haystack.find(needle)` 可以在字符串里面查找字符串的位置，没有则返回-1，或者用`haystack.split(needle)[0]`分割，并选取[0]

4.29 
今天听师兄说，CV岗位很难找到工作
考虑学C++

* 387 字符串中第一个唯一字符串
跟次数有关的，统一字典建立，遍历字符串，从字典中找键值等于1的

* 819 最常见的单词
先用空格replace符号，再转换成小写，split(),遍历列表，过滤掉在banned中的，更加简洁字典存取次数的写法` if i not in dic:dic[i] = 0 dic[i] += 1`
最后返回字典中value值最大的key`max(dic,key= lambda x : dic[x])`

* 14 最长公共前缀
题解里面的解题思路很多，先找出两个的公共前缀`while strs[i].find(res) != 0:res = res[:-1]`起始坐标必为0,然后再往后比较

* 680 验证回文字符串 II
先判断是否回文，然后用双指针判断当l,r左右指针不等的时候，判断`a = s[l+1:r+1] b = s[l:r]`是否可以反转，然后确定删除l,r

* 686 重复叠加字符串匹配
先用集合判断会快很多，`len(set(A)) < len(set(B))`,边界条件是`while len(A*i) <len(A+A+B):`之前太耿直的遍历，超时

* 859 亲密字符串
A和B的长度如果不相等或者小于2，返回假，有两种情况:1、A==B 只有全部一样，才返回真 2、A ！= B,找出 A[i] !=B[i]的列表 ，判断`a == b[::-1]`


