#985 查询后的数组和
class Solution:
    def sumEvenAfterQueries(self,A,queries):
      #A: List[int], queries: List[List[int]]) -> List[int]
      B = []
      for i in range(len(queries)):
          val = queries[i][0]
          ind = queries[i][1]
          A[ind] += val
          # print(A[ind])
          B.append(sum(i for i in A if i % 2 == 0))
      return B





