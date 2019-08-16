# 73.矩阵置零
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for m in range(col):
                        matrix[i][m] = ""
                    for n in range(row):
                        matrix[n][j] = ""

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "":
                    matrix[i][j] = 0

