# 387. 字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self, s):
            # s: str) -> int:
            dic = {}
            for i in range(len(s)):
                if s[i] not in dic:
                    dic[s[i]] = 1
                else:
                    dic[s[i]] += 1
            for i in range(len(s)):
                if dic[s[i]] == 1 :
                    return i

            return -1