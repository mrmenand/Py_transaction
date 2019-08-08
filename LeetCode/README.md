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

##  日彔 

7.11 

* 78 子集  
   - 组合：` [list(tmp)  for i in range(len(nums)+1) for tmp in itertools.combinations(nums,i)] `  
   - 位掩码： [回溯+位源码题解](https://leetcode-cn.com/problems/subsets/solution/hui-su-python-dai-ma-by-liweiwei1419/) 
   - 迭代 
   - 回溯：[回溯算法题解](https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/) 

* 950 按递增顺序显示 
当找不到规律时候，尝试倒着推
  ```
  if ret: ret.insert(0,i)
  ret.append(i) 
 ```

8.8 
最近状态不太行，今天开始继续刷题  
* 216 组合总结 III 
回溯、剪枝，类似与栈的递归出栈入栈，不可以重复

* 39 组合总和 
回溯，可以重复