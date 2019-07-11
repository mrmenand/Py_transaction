# 119. 杨辉三角 II
class Solution:
    def getRow(self,rowIndex):
       # rowIndex: int) -> List[int]:
       res = []
       for i in range(1, rowIndex + 2):
           if i == 1:
               res.append([1])
           else:
               temp = []
               for j in range(i):

                   if j == 0 or j == i - 1:
                       temp.append(1)
                   else:
                       temp.append(res[i - 2][j - 1] + res[i - 2][j])
               res.append(temp)

       return  res[rowIndex]

test = Solution()
print(test.getRow(rowIndex=3))