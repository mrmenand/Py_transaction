# 1009. 十进制整数的反码
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int("".join(["0" if i == "1" else "1" for i in bin(N)[2:]]), 2)