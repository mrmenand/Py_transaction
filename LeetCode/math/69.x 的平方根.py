# 69. x 的平方根
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        left, right = 1, x // 2
        while left < right:
            mid = (left + right + 1) >> 1
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid

        return left
