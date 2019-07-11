# 643. 子数组最大平均数 I
class Solution:
    def findMaxAverage(self,num,k):
            # nums: List[int], k: int) -> float:
            s = sum(num[:k])
            m = s

            for i in range(k,len(num)):
                s = s + num[i] - num[i-k]
                if m < s :
                    m = s
            return m/k


