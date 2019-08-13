# 38. 报数
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        length = 0
        num, ret = "", ""
        for char in self.countAndSay(n - 1):
            if char != num:
                if length > 0:
                    ret += str(length) + num
                length = 1
                num = char
            else:
                length += 1

        ret += str(length) + char

        return ret

# class Solution:
#     def countAndSay(self, n):
#         # n: int) -> str:
#         s = "1"
#         for i in range(1, n):
#             length = 1
#             result = ""
#             for j in range(len(s)):
#                 if j < len(s) - 1 and s[j] == s[j + 1]:
#                     length += 1
#                 else:
#                     result += str(length) + s[j]
#                     length = 1
# 
#             s = result
# 
#         return s
