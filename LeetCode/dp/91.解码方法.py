# 91. 解码方法
from functools import lru_cache

class Solution:
    @lru_cache()
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        res = 0
        if len(s) >= 1 and s[0] != "0":
            res += self.numDecodings(s[1:])
        if len(s) >= 2 and s[0] != "0" and int(s[:2]) <= 26:
            res += self.numDecodings(s[2:])

        return res
