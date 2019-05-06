# 463. 岛屿的周长
class Solution(object):
    def islandPerimeter(self, grid):
        for row in grid:
            row.insert(0, 0)
            row.append(0)

        grid.insert(0, [0] * len(grid[0]))
        grid.append([0] * len(grid[0]))

        edge = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 1:
                    edge += (4 - grid[i + 1][j] - grid[i - 1][j] - grid[i][j + 1] - grid[i][j - 1])

        return edge
