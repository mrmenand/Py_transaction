# 387. 字符串中的第一个唯一字符
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s):
        dic = OrderedDict()
        for i in s:
            dic[i] = dic.get(i,0) + 1

        for k,v in dic.items():
            if v == 1:
                return s.index(k)

        return -1

# class Solution:
#     def firstUniqChar(self, s):
#             # s: str) -> int:
#             dic = {}
#             for i in range(len(s)):
#                 if s[i] not in dic:
#                     dic[s[i]] = 1
#                 else:
#                     dic[s[i]] += 1
#             for i in range(len(s)):
#                 if dic[s[i]] == 1 :
#                     return i
#
#             return -1