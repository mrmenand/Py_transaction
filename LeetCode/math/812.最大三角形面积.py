# 812. 最大三角形面积
from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        m_area = 0
        for i in combinations(points, 3):
            x = [i[0][0], i[1][0], i[2][0]]
            y = [i[0][1], i[1][1], i[2][1]]

            s = abs((x[0] - x[2]) * (y[1] - y[2]) -
                    (x[1] - x[2]) * (y[0] - y[2])) / 2
            m_area = max(m_area, s)

        return m_area
