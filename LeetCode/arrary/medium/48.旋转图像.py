class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = Solution()
a.rotate(matrix)
print(matrix)
