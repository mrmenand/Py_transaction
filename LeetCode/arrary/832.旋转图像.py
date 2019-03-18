#832旋转图像
class Solution:
    def flipAndInvertImage(self, A):
        # A: List[List[int]]) -> List[List[int]]
        B=[]
        for i in range(len(A)):
            # print(A[i][::-1])
            B.append(A[i][::-1])
            for j in range(len(B[i][:])):
                if B[i][j] ==0:
                    B[i][j] =1
                else:
                    B[i][j] =0

        return B

# class Solution:
#     def flipAndInvertImage(self, A):
#         # 1 flip
#         for i, p in enumerate(A):
#             A[i] = list(reversed(p))
#             # 2 invert
#             for j, v in enumerate(A[i]):
#                 if A[i][j] is 0:
#                     A[i][j] = 1
#                 else:
#                     A[i][j] = 0
#
#         return A

A = [[1,1,0],[1,0,1],[0,0,0]]
test = Solution()
print(test.flipAndInvertImage(A))