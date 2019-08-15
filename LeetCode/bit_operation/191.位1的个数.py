# 191. 位1的个数
class Solution(object):
    def hammingWeight(self, n):
        cnt = 0
        while n:
            cnt += (n & 1)
            n >>= 1
        return cnt