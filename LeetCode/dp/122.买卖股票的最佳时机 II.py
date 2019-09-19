# 122. 买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, price):
        # prices: List[int]) -> int:
        result = 0
        for i in range(1, len(price)):
            if price[i] - price[i - 1] > 0:
                result += price[i] - price[i - 1]

        return result

# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if prices == []:
#             return 0
#         minp = prices[0]
#         buy = False
#         buy_price = 0
#         profit = 0
#         n = len(prices)
#         for i in range(n):
#             if i == n-1:
#                 if buy == True:
#                     profit += prices[i] - buy_price
#             elif prices[i] < prices [i+1] and buy == False:
#                 buy = True
#                 buy_price = prices[i]
#             elif prices[i] > prices[i+1] and buy == True:
#                 profit += prices[i] - buy_price
#                 buy = False
#         return profit
