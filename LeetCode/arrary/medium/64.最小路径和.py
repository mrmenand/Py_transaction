# 64 最小路径和
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if j and i:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
                elif i:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                elif j:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
