# 883. 三维形体投影面积
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy, xz, yz = 0, 0, 0
        for i in grid:
            xz += max(i)
            xy += len(grid) - i.count(0)

        for i in zip(*grid):
            yz += max(i)

        print()
        return xz + yz + xy
