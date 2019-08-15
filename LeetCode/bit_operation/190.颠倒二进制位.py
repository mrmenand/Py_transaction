# 190. 颠倒二进制位
class Solution:
    def reverseBits(self, n):
        cnt, ret = 32, 0
        while cnt:
            ret <<= 1
            ret |= (n & 1)
            n >>= 1
            cnt -= 1
        return ret
