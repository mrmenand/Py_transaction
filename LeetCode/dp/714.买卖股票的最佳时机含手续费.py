# 714. 买卖股票的最佳时机含手续费
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        profit, mins = 0, prices[0]
        for i in range(1, n):
            if prices[i] < mins:
                mins = prices[i]
            elif prices[i] > mins + fee:
                profit += prices[i] - fee - mins
                mins = prices[i] - fee

        return profit
# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         buy, sell = float("-inf"), 0
#
#         for price in prices:
#             buy, sell = max(sell - price - fee, buy), max(buy + price, sell)
#
#         return sell
