# 74. 搜索二维矩阵
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) >> 1
            i, j = mid // n, mid % n
            if matrix[i][j] < target:
                left += 1
            elif matrix[i][j] > target:
                right -= 1
            else:
                return True

        return False
