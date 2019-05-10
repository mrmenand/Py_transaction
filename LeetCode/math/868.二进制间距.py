# 868. 二进制间距
class Solution:
    def binaryGap(self, N: int) -> int:
        b = bin(N)[2:]
        last_one, res = 0, 0
        for i, v in enumerate(b):
            if v == "1":
                res = max(res, i - last_one)
                last_one = i

        return res
