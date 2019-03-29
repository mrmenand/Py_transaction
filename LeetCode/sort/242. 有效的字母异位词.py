# 242. 有效的字母异位词
class Solution:
    def isAnagram(self,s,t):
            # s: str, t: str) -> bool:
          return sorted(s) == sorted(t)

# 以下方法更具备通用性
# class Solution:
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         from collections import Counter
#         return Counter(s) == Counter(t)