# 171. Excel表列序号
class Solution:
    def titleToNumber(self, s: str) -> int:
       value = 0
       for i, v in enumerate(s):
           value += 26 ** (len(s)-i-1) * (ord(v) - 64)

       return value
