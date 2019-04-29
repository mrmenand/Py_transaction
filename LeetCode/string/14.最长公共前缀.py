# 14. 最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
            # strs: List[str]) -> str:
            if not strs:
                return ""

            res = strs[0]
            i = 1

            while i < len(strs):
                ## 起始坐标为0
                while strs[i].find(res) != 0:
                    res = res[:-1]
                i += 1

            return res