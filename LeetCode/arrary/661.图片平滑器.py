# 661.图片平滑器
# class Solution:  ##理解错题目，角除四，边除6，但是这种解题思路才具有一般性
#     def imageSmoother(self, M):
#                       # M: List[List[int]]) -> List[List[int]]:
#              new_M = []
#              for i in range(len(M)+2):
#                  temp =[]
#                  if i==0 or i==len(M)+1:
#                      temp=[0]*(len(M[0])+2)
#                      new_M.append(temp)
#                  else:
#                      temp=[0] +M[i-1]+[0]
#                      new_M.append(temp)
#              res = []
#              for i in range(1,len(new_M)-1):
#                  tep = []
#                  for j in range(1, len(new_M[0])-1):
#                      average =(new_M[i][j]+new_M[i][j+1]+new_M[i][j-1]+new_M[i+1][j]
#                                +new_M[i+1][j+1]+new_M[i+1][j-1]+new_M[i-1][j]+new_M[i-1][j+1]+new_M[i-1][j-1])//9
#                      tep.append(average)
#                      # print(tep)
#                  res.append(tep)
#
#              return res
class Solution:  ###没有考虑到只有一行，或者一列的情况
    def imageSmoother(self, M):
                      # M: List[List[int]]) -> List[List[int]]:
             new_M = []
             for i in range(len(M)+2):
                 temp =[]
                 if i==0 or i==len(M)+1:
                     temp=[0]*(len(M[0])+2)
                     new_M.append(temp)
                 else:
                     temp=[0] +M[i-1]+[0]
                     new_M.append(temp)
             print(new_M)
             res= []
             l = len(new_M[0]) - 1
             h = len(new_M) - 1
             for i in range(1, h):
                  tep = []
                  for j in range(1, l):

                      if (i==1 and j==l-1) or (i==1 and j==1) or (i==h-1and j==1) or (i==h-1and j==l-1):
                          average = (new_M[i][j] + new_M[i][j + 1] + new_M[i][j - 1] + new_M[i + 1][j]
                                                                    +new_M[i+1][j+1]+new_M[i+1][j-1]+new_M[i-1][j]+new_M[i-1][j+1]+new_M[i-1][j-1])//4
                          tep.append(average)
                      elif i==1 or i==h-1 or j==1 or j==l-1:
                          average = (new_M[i][j] + new_M[i][j + 1] + new_M[i][j - 1] + new_M[i + 1][j]
                                     + new_M[i + 1][j + 1] + new_M[i + 1][j - 1] + new_M[i - 1][j] + new_M[i - 1][
                                         j + 1] + new_M[i - 1][j - 1]) // 6
                          tep.append(average)
                      else:
                          average = (new_M[i][j] + new_M[i][j + 1] + new_M[i][j - 1] + new_M[i + 1][j]
                                     + new_M[i + 1][j + 1] + new_M[i + 1][j - 1] + new_M[i - 1][j] + new_M[i - 1][
                                         j + 1] + new_M[i - 1][j - 1]) // 9
                          tep.append(average)

                  res.append(tep)
             return res


test =Solution()
print(test.imageSmoother(M=[[1]]))