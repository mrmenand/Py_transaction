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
   
8.12    
* 238 除自身以外数组的乘积
  - O(n)，左边乘积*右边乘积 
  - 上下三角形，对角线为1 
 
 
 8.13 
 * 64 最小路径和 
  - 动态规划 
  
 8.14 
 * 442 数组中重复的数据
   -  对应位置的数字取负数 如果发现已经是负数 说明这个下标是重复的。
   
8.15 
* 120 三角形最小路径和 
   - 自底向上，动态规划  
  
8.16 
* 287 寻找重复数 
  - 可以类似268的位运算（异或） 
  - 哈希表 
 
8.17 
* 105 从前序与中序遍历序列构造二叉树 
  - 类似106，按前序遍历的顺序每次pop并建立节点root，在中序遍历中找到root的对应index，划分出哪些节点构成此节点的左子树inorder[:i]，哪些构成右子树inorder[i+1:]
  - 可以使用哈希表减少时间 
  

8.18 
* 960 煎饼排序 
  - 先找最大的，反转到头部，再逆序反转 
  
8.19 
* 11 盛最多水的容器 
   - 双指针   

8.20 
总是想的太多，做的太少  


8.27
每日一题还是要继续下去的 
* 667 优美的排列 II 
  - 更多的找规律吧，正序后反转  
  
8.28 

* 90 子集II 
   - 与78题相比，加了重复元素，若新遍历元素是刚刚遍历过的
   - 递归回溯 
  

8.29 
* 40 组合总和 II 
   - 与39题相比，每个数字只能出现一次，针对与不能含有重复组合的问题，与90题类似，对数组进行升序排序后进行坐标判断  
    - 递归回溯 
   
   
8.30 

一转眼，十年过，秋千落，偶尔的感受来自聚会上的花田错 -- BOOM 

* 16 最接近的三数之和 
   - 排序后固定一个数，利用双指针对撞 
  
8.31 

* 18 四数之和 
   -  固定两个数，用双指针找另外两个数，与三数之和的类似 
   - 利用剪枝直接排除重复解 
   - 合理移动双指针直接排除非正确解  
   
9.2 

* 54 旋转矩阵  
   - 与59 旋转矩阵II 和 48 旋转图像是同类型的题目
   -  将已经走过的地方置0，通过求余的方式判断是否走过 
   `matrix[(i + di) % row][(j + dj) % col] == 0`


9.3 
* 63 不同的路径 II 
   - 与62题相似，左面和上面各加一个障碍边 
   - 动态规划 

9.4 
岁月如歌，当下如酒，且醉且饮 

* 74 搜索二维矩阵 
  - 有序查找，二分查找，在left <= right 的=循环退出条件错了很多次   
  
9.5 

* 80 删除排序数组中的重复项 II 
    - 原地删除 通过 nums[i] = nums 和变量 i 控制 
    
9.6 

* 81 搜索旋转排序数组 II
  - 33题的提升题，加了重复元素，需要在相等的元素内进行判断 

9.7 

* 152 乘积最大子序列
  - 动态规划，遍历nums过程，对正负和之前的结果进行分情况讨论  
  
9.8 

* 153 寻找旋转排序数组中的最小值
  - 二分搜索的适用情况：有序（部分有序）序列 
  

9.9 
* 209 长度最小的子数组
     - 滑动窗口，遍历  
    
9.10 

* 228 汇总区间 
    -  双指针  
    
9.11 

* 229 求众数 II 
   - 哈希表 
   
9.12  
* 495 提莫攻击 
  - 攻击间隔和持续时间的条件判断 
  
9.13 
- 560 和为K的子数组 
  - 哈希表，计算数组中第i个元素到第j个元素的和 sum(nums[i:j])，
   
9.14 
* 565  数组嵌套 
    - 求环的最大路径，利用一个visited进行是否访问的判断 

9.15 

* 611 有效三角形的个数 
   - 双指针，两边之和大于第三边 
 

9.16 
*  670 最大交换  
   - 贪心算法，从右到左扫描最大索引的数字，然后交换 

9.17 
*  695 岛屿的最大面积 
   - 与200题岛屿数量题目一致，变成计数面积，（可以加个访问数组进行优化）
   - 着色思想  
   
   
9.18 
* 713 乘积小于K的子数组 
   - 双指针 
   
9.19 
* 714 买卖股票的最佳时机含手续费 
    - 动态规划 
    - 贪心算法 （假设此次交易利润：B - A - fee， 下次交易利润：D - C - fee）
    - 需要总结 买股票问题 

9.20 
* 718 最长重复子数组 
   - 动态规划 
   - 移尺法

9.21 
* 729 我的日程安排表 I  
   - 简单设计题，也可以用二分搜索优化 



