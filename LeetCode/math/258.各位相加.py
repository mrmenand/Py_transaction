# 258. 各位相加
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
             num = sum(int(i) for i in str(num))
        return num
