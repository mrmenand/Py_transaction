# 746. 使用最小花费爬楼梯
class Solution:
    def minCostClimbingStairs(self,cost):
          # cost: List[int]) -> int:
          cur,pre_cur = 0, 0
          for i in range(2,len(cost)+1):
              pre_cur,cur = cur,min(cur+cost[i-1],pre_cur+cost[i-2])

          return cur
