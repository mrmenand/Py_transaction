# 867. 转置矩阵
class Solution:
    def transpose(self, A):
            # A: List[List[int]]) -> List[List[int]]
            B = []
            for j in range(len(A[0])):
                row = []
                for i in range(len(A)):
                    row.append(A[i][j])
                B.append(row)

            return  B

A =[[1,2,3],[4,5,6],[7,8,9]]
test = Solution()
print(test.transpose(A))

# class Solution:
#     def transpose(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         A[:] = map(list,zip(*A))
#         return A