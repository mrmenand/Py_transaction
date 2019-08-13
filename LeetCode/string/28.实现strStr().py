# 28. 实现strStr()
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

# class Solution:
#     def strStr(self, haystack, needle):
#             # haystack: str, needle: str) -> int:
#             if not needle:
#                 return 0
#             return haystack.find(needle)