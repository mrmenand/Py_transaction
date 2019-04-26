# 551. 学生出勤记录 I
class Solution:
    def checkRecord(self, s):
            # s: str) -> bool:
            if s.count("A") > 1:
                return False
            for i in range(len(s)):
                if i < len(s)-2 and s[i] == s[i+1] == s[i+2] == "L":
                    return False

            return True  