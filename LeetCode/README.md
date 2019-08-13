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

8.9 
* 289 生命游戏 
  - 防止边界溢出，padding 
  - 位运算 ，原棋盘的最后一位保存生命信息 ，通过左移右移保存和恢复信息 
  
8.10 
* 48 旋转图像 
   - 先转置后反转 
   - 旋转两个矩形  
   
8.11 
* 106 从中序与后序遍历序列构造二叉树 
   - 左根右 inorder[:idx],postorder[:idx]
   - 左右根 inorder[idx+1:],postorder[idx:] 
   
* 238 除自身以外数组的乘积
  - O(n)，左边乘积*右边乘积 
  - 上下三角形，对角线为1 
 
 
 8.12 
 * 64 最小路径和 
  - 动态规划