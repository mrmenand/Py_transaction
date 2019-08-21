# 29.两数相除
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ret = 0
        flag = 1 if dividend ^ divisor >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        while divisor <= dividend:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                ret += i
                i <<= 2
                tmp <<= 2

        ret = ret * flag

        return min(max(-2 ** 31, ret), 2 ** 31 - 1)
