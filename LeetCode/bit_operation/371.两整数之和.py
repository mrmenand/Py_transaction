# 371. 两整数之和
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            a, b = (a ^ b) % 0x100000000, ((a & b) << 1)%0x100000000

        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)
