# 240. 搜索二维矩阵 II
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            ver = self.bisert(matrix, target, i, True)
            hor = self.bisert(matrix, target, i, False)
            if ver or hor:
                return True

        return False

    def bisert(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) >> 1
            if vertical:
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        return False

# class Solution:
#     def searchMatrix(self, matrix, target):
#         if not matrix or not matrix[0]:
#             return False
#         row, col = len(matrix), len(matrix[0])
#         x, y = row - 1, 0
#         while x >= 0 and y < col:
#             if matrix[x][y] > target:
#                 x -= 1
#             elif matrix[x][y] < target:
#                 y += 1
#             else:
#                 return True
#         return False
