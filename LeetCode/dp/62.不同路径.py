# 62. 不同路径
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m] + [[1] + [0] * (m - 1) for i in range(n - 1)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


print(Solution().uniquePaths(7, 3))