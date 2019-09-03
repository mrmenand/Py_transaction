# 63. 不同路径 II
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]

        return dp[-2]
