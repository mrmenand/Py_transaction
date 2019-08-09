# 118.杨辉三角
class Solution:
    def generate(self, numRows):
        ret = [[1] * i for i in range(1,numRows+1)]
        for i in range(2,numRows):
            for j in range(1,i):
                ret[i][j] = ret[i-1][j] + ret[i-1][j-1]
        return ret


# class Solution:
#     def generate(self, numRows):
#         # numRows: int) -> List[List[int]]:
#          res = []
#          for i in range(1,numRows+1):
#              if i==1:
#                  res.append([1])
#              else:
#                  temp = []
#                  for j in range(i):
#
#                      if j==0 or j==i-1:
#                          temp.append(1)
#                      else:
#                          temp.append(res[i-2][j-1]+res[i-2][j])
#                  res.append(temp)
#
#          return res




# class Solution:
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         L = []
#         if numRows == 0:
#             return L
#         for i in range(numRows):
#             L.append([1])
#             for j in range(1,i+1):
#                 if j==i:
#                     L[i].append(1)
#                 else:
#                     L[i].append(L[i-1][j]+L[i-1][j-1])
#         return L