# 242. 有效的字母异位词


class Solution:
    def isAnagram(self,s,t):
        dic_s,dic_t = {},{}
        for i in s :
            dic_s[i] = dic_s.get(i,0) + 1

        for i in t:
            dic_t[i] = dic_t.get(i, 0) + 1

        if len(dic_s) != len(dic_t):
            return False
        else:
            for i in dic_s:
                if dic_s[i] != dic_t.get(i,0):
                    return False
        
        return True
        
# class Solution:
#     def isAnagram(self,s,t):
#             # s: str, t: str) -> bool:
#           return sorted(s) == sorted(t)


# class Solution:
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         from collections import Counter
#         return Counter(s) == Counter(t)