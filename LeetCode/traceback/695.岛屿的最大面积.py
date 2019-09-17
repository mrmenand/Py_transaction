# 695. 岛屿的最大面积
class Solution:
    flag = 0
    maxs = 0

    def draw(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
            grid[x][y] = 0
            self.flag += 1
            self.draw(grid, x, y + 1)
            self.draw(grid, x, y - 1)
            self.draw(grid, x + 1, y)
            self.draw(grid, x - 1, y)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.flag = 0
                    self.draw(grid, i, j)
                    self.maxs = max(self.flag, self.maxs)

        return self.maxs
