# 459. 重复的子字符串
class Solution:
    def repeatedSubstringPattern(self, s):
             # s: str) -> bool:
             for i in range(1,len(s)//2+1):
                 if s[i] == s[0] and s[:i] * (len(s)//i) == s:
                     return True

             return False
