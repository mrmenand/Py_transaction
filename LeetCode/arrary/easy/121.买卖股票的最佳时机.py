# 121.买卖股票的最佳时机


# class Solution:  #测试样例过了，提交报错，用动态规划的思想
#     def maxProfit(self, prices):
#         # prices: List[int]) -> int:
#          res = []
#          for i in range(len(prices)-1):
#              for j in range(i,len(prices)):
#                  res.append(prices[j]-prices[i])
#
#          return max(res)
class Solution:
    def maxProfit(self, prices):
        # prices: List[int]) -> int:
        min_p = 2**31
        max_p = 0
        for i in range(len(prices)):
            min_p = min(min_p,prices[i])
            max_p = max(max_p,prices[i]-min_p)

        return max_p

# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if prices == []:
#             return 0
#         minp = prices[0]
#         profit = 0
#         n = len(prices)
#         for i in range(1, n):
#             if prices[i] < minp:
#                 minp = prices[i]
#             elif prices[i] - minp > profit:
#                 profit = prices[i] - minp
#         return profit
test = Solution()
print(test.maxProfit(prices=[7,6,4,3,1]))