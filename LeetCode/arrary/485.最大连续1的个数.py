# 485. 最大连续1的个数
class Solution:
    def findMaxConsecutiveOnes(self, nums):
                   # nums: List[int]) -> int:
                  res = []
                  cnt = 0
                  for i in nums:
                      if i ==1:
                          cnt+=1
                      else:
                          res.append(cnt)
                          cnt =0
                  res.append(cnt)
                  return max(res)


