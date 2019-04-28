# 125. 验证回文串
class Solution:
    def isPalindrome(self, s):
            # s: str) -> bool:
            s = "".join(filter(str.isalnum, s)).lower()
            return  s == s[::-1]
