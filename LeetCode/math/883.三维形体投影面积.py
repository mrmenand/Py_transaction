# 883. 三维形体投影面积
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x, y, z = 0, 0, 0
        n = len(grid)
        for i in grid:
            x += n - i.count(0)
            z += max(i)

        for i in zip(grid):
            y += max(i)

        return x + y + z

