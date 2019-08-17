# 200. 岛屿数量
import functools

class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        marked = [[False] * m for _ in range(n)]
        cnt = 0

        for i in range(n):
            for j in range(m):
                if not marked[i][j] and grid[i][j] == "1":
                    cnt += 1
                    self.traceback(grid, i, j, m, n, marked)

        return cnt

    def traceback(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < n and 0 <= new_j < m and not marked[new_i][new_j] and grid[new_i][new_j] == "1":
                self.traceback(grid, new_i, new_j, m, n, marked)
