# 121.买卖股票的最佳时机

class Solution:
    def maxProfit(self, prices):
        cost,profit = float("inf"),0
        for price in prices:
            cost = min(price,cost)
            profit = max(price-cost,profit)
        return profit


# class Solution:  #测试样例过了，提交报错，用动态规划的思想
#     def maxProfit(self, prices):
#         # prices: List[int]) -> int:
#          res = []
#          for i in range(len(prices)-1):
#              for j in range(i,len(prices)):
#                  res.append(prices[j]-prices[i])
#
#          return max(res)
test = Solution()
print(test.maxProfit(prices=[7,6,4,3,1]))