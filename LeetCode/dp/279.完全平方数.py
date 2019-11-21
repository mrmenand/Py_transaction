# 279. 完全平方数
from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        if n <= 0:
            return False
        queue = deque([n])
        step = 0
        visited = set()

        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.pop()
                for i in range(1, int(tmp ** 0.5) + 1):
                    diff = tmp - i ** 2
                    if diff == 0:
                        return step
                    if diff not in visited:
                        visited.add(diff)
                        queue.appendleft(diff)
        return step

if __name__ == '__main__':
    print(Solution().numSquares(n=12))


# class Solution:
#     @lru_cache()
#     def numSquares(self, n: int) -> int:
#         dp = [float("inf") for _ in range(n+1)]
#         dp[0] = 0
#         for i in range(1, n + 1):
#             for j in range(1, int(i ** 0.5) + 1):
#                 dp[i] = min(dp[i], dp[i - j * j] + 1)
#
#         return dp[-1]
