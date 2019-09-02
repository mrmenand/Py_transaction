# 54. 螺旋矩阵
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ret = []
        row, col = len(matrix), len(matrix[0])
        i, j, di, dj = 0, 0, 0, 1
        for _ in range(row * col):
            ret.append(matrix[i][j])
            matrix[i][j] = 0
            if matrix[(i + di) % row][(j + dj) % col] == 0:
                di, dj = dj, -di

            i += di
            j += dj

        return ret
