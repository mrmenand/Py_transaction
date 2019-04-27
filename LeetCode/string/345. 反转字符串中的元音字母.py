# 345. 反转字符串中的元音字母
class Solution:
    def reverseVowels(self, s):
        l, r = 0, len(s)-1
        list_s = list(s)
        while l < r:
            if list_s[l] in "aeiouAEIOU" and list_s[r] in "aeiouAEIOU":
                list_s[l], list_s[r] = list_s[r], list_s[l]
                l += 1
                r -= 1
            if list_s[l] not in "aeiouAEIOU":
                l += 1
            if list_s[r] not in "aeiouAEIOU":
                r -= 1
        return    "".join(list_s)


# class Solution:
#     def reverseVowels(self, s):
#                 # s: str) -> str:
#                 # tmp = []
#                 # for i in range(len(s)):
#                 #     if s[i] in "aeiouAEIOU":
#                 #         tmp.append(i)
#                 # for j in range(len(tmp)//2):
#                 #     k = len(tmp)-1-j
#                 #     s = s[:j] + s[k] + s[j+1:k] + s[j]
#                 #
#                 # return s
