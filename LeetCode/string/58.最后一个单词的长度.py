# 58. 最后一个单词的长度
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
             return 0 if s.split() == [] else len(s.split()[-1])