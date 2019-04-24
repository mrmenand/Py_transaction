# 557. 反转字符串中的单词 III
class Solution:
    def reverseWords(self,s):
            # s: str) -> str:
            list_s = s.split()
            for i in range(len(list_s)):
                list_s[i] = list_s[i][::-1]
            return " ".join([j for j in list_s])
