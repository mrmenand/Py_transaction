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
- [Shortest-LeetCode-Python-Solutions](https://github.com/cy69855522/Shortest-LeetCode-Python-Solutions)

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

4.30 四月是你的谎言呀，我也出生在这一天呀
* 206 反转列表
cur指向的是链表的节点，利用多元赋值`pre, pre.next, cur = cur, pre, cur.next`

* 876 链表的中间结点
题解里有用数组存取单链表结点、` while A[-1].next:A.append(A[-1].next)` 返回列表长度//2时的存的节点  虎躯一震听闻双指针里面有一种快慢指针
fast是slow指针遍历的两倍，当快速指针到头，返回slow指针，边界条件很重要`while fast and fast.next:`

*  21 合并两个有序链表
`node = res = ListNode(None)`用一个空结点作为头结点，最后返回res.next，**其实有点不懂node指向的是res,node有变化为什么res也有变化**。判断l1.val和l2.val的大小,赋值并指向下一个结点 ，l2和l1存在长度不一样，还要判断

* 83 删除排序链表的重复元素
`while node and node.next` 判断当前结点和下一个结点的值是否相等，指向下一个

* 160 相交链表
a + b == b + a 保证长度一样，是结点（物理地址）一样而不是结点值一样

* 141 环形链表
快慢指针，边界条件是：`while fast and fast.next:`，当fast == slow时，返回真

* 234 回文链表
利用栈储存值，判断是否相等`stack.append(node.val)`,反转判断，听说快慢指针也可以

5.5  
好吧，摸鱼了四天，罪恶感
发现手有点生
* 811 子域名的访问计数
先分割，再对域名分割，依次从后往前遍历，`dic[tmp] = dic.get(tmp,0) + int(num)` ,  遍历字典用`dic.item()`

5.6
昨天生日，恰烧烤去了
又见罪恶

* 136 只出现一次的数字 
**Def : 0 ^ N = N，N ^ N = 0** 异或操作相异为1，交换律，最后返回结果

* 463 岛屿的周长
遇见判断边界的条件，在外面加一圈0,问题转化为当grid[i][j] ==1 时，判断邻近四个点是否有1，` edge += (4 - grid[i + 1][j] - grid[i - 1][j] - grid[i][j + 1] - grid[i][j - 1])`

* 575 分糖果
马冬梅会遇见三中情况`min(len(set(candies)),len(candies)//2)`

* 389 找不同
找一个的不同，可以利用0和数字异或为数字，` for i in s+t : res = res ^ ord(i)` ,还有一种就是减法chr(sum([ord(i) for i in t] )- sum([ord(j) for j in s])))

* 447 回旋镖的数量
计算其他点到当前点的距离，如果相同距离的点有2个以上则满足$ A_n ^2$

* 953 验证外星语词典
`words == sorted(words, key = lambda x: [order.index(i)  for i in x])`利用lambda函数

5.7
时间太快，但是我也一直在

* 748 提交的代码
两种过滤的方式，一种用列表推导式：`newPlate = [ i.lower() for i in licensePlate if i.isalpha()]`,第二种用过滤器`newPlate = filter(str.isalpha,str(licensePlate.lower()))`,对words的长度进行排序，遍历word的每一个字符，与newplate比较，最后判断长度

* 609 员工的重要性
BFS: `hashmap[employee.id] = [employee.importance, employee.subordinates]` 建立哈希表，然后栈来遍历，res += hashmap[emp][0]     DFS `self.res += hashmap[sub][0] , dfs(hashmap[sub][1])`

* 409 最长回文串
建立哈希表，遍历表键值，对%2判断，是则加上，不是`cnt + = v-1  `并且把one = 1，最后返回结果cnt + one

* 599 两个列表的最小索引总和
利用set集合寻找共同`common = set(list1) & set(list2)`，因为是无序，用哈希表存取索引值的，找到最小的索引值，最后返回键值与最小的key列表`[i for i in hashmap if hashmap[i] == minidx]`

* 205 同构字符串
利用两个哈希表建立s，t 储存索引，判断s和t中每个字母最后出现的位置是否相同，不相同则不同构，顺序很关键`  if hash_s[s[i]] != hash_t[t[i]]: return False \n hash_s[s[i]] = i \n hash_t[t[i]] = i`

* 594 最长和谐子序列
利用Counter建立的哈希表默认是降序的，遍历数组，如果比nun大的在哈希表里面，`res = max(res,hashmap[num] + hashmap[num+1])`

* 5.8 
生活呀，总是有一些烦心事，但也正是生活呀

* 290 单词模式
用哈希表建立列表pattern的映射关系，首先判断`if pattern[i] not in hashmap:`再判断` if words[i] not in hashmap.values()`建立表，对在表中的pattern[i]进行`hashmap[pattern[i]] != words[i]:`

* 970 强整数
暴力破解，但是对遍历的边界进行限` max_x = 1 if x == 1 else int(math.log(bound,x))+1`,不然在x=1,y=2,bound=1000这个样例会超时

* 438 找到字符串所有字母的异位词
滑窗法： 想象一个窗口在s上向右移动,窗口宽度为len(p)， 只要窗口内的字符串各字符数量与p中一致,则匹配成功，窗口在向右移动的时候,只需要将最左端的值从字典中删除,将最右端+1的值加入字典即可。` if i-n+1 >= 0 :hs[s[i-n+1]] = hs.get(s[i-n+1])-1; if hs[s[i-n+1]] == 0:del hs[s[i-n+1]]`

* 645 错误的集合
只有一位的不同，与358题目类似。利用sum找出不同的` return [sum(nums) - sum(set(nums)),sum(set(range(1, len(nums)+1)) - set(nums))]`

* 245 计算质数
用的是厄拉多塞筛法.：先将 2－N 的各数放入表中，然后在 2 的上面画一个圆圈，然后划去 2 的其他倍数；第一个既未画圈又没有被划去的数是 3，将它画圈，再划去 3 的其他倍数；现在既未画圈又没有被划去的第一个数是 5，将它画圈，并划去5的其他倍数……依次类推，一直到所有小于或等于N的各数都画了圈或划去为止
`for i in range(2,int(n**0.5)+1):if prime[i]: prime[i * i:n:i] = [0] * len(prime[i * i:n:i])`






