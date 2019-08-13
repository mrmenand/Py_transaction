# 14. 最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        ret = [i for i in map(set,zip(*strs))]
        res = ""
        for i,str in enumerate(ret):
            str = list(str)
            if len(str) > 1:
                break
            res += str[0]

        return res

# class Solution:
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""
#         s1,s2 = max(strs),min(strs)
#         for i ,str in enumerate(s2):
#             if  str != s1[i]:
#                 return s1[:i]
#
#         return s2



# class Solution:
#     def longestCommonPrefix(self, strs):
#             # strs: List[str]) -> str:
#             if not strs:
#                 return ""
#
#             res = strs[0]
#             i = 1
#
#             while i < len(strs):
#                 ## 起始坐标为0
#                 while strs[i].find(res) != 0:
#                     res = res[:-1]
#                 i += 1
#
#             return res