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




