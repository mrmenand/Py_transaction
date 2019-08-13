# 7.整数反转
class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            ret = int(str(x)[::-1])
        else:
            ret = -int(str(-x)[::-1])

        if ret < - 2 ** 31 or ret > 2 ** 31 - 1:
            return 0
        return ret

