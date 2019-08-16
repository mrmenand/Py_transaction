# 3. 无重复字符的最长子串

"""双指针"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s :
            return 0
        left,right = 0 ,0
        max_length = 0
        for c in s:
            if c not in s[left:right]:
                right += 1
            else:
                left += s[left:right].index(c) + 1
                right += 1

            max_length = max(right - left,max_length)

        return max_length





"""容器"""
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
#         windows = []
#         max_length = 0
#
#         for c in s:
#             if c not in windows:
#                 windows.append(c)
#             else:
#                 windows[:] = windows[windows.index(c) + 1:]
#                 windows.append(c)
#
#             max_length = max(len(windows), max_length)
#
#         return max_length
