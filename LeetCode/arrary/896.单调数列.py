##866 单调数列
class Solution:
    def isMonotonic(self, A):
                    # A: List[int]) -> bool:
                  if A ==sorted(A) or A==sorted(A,reverse=True):
                      return  True
                  else:
                      return False
                  # return A ==sorted(A) or A==sorted(A,reverse=True)  一句话得出答案

test = Solution()
print(test.isMonotonic(A=[6,5,4,4]))