# 326. 3的幂
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ret = 1
        while ret < n:
            ret *= 3

        return ret == n

