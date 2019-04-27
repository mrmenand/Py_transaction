# 541. 反转字符串 II
class Solution:
    def reverseStr(self,s,k):
            # s: str, k: int) -> str:
            res = ""
            n = len(s)//k
            for i in range(1,n+1):
                if i % 2 == 1:
                     res += s[(i-1)*k:i*k][::-1]
                else:
                     res += s[(i-1)*k:i*k]

            if n % 2 == 0:
                res += s[n*k:][::-1]
            else:
                res += s[n*k:]

            return res

# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         res = ''
#         for i in range(0,len(s),2*k):
#             print(i)
#             res+=s[i:i+k][::-1]+s[i+k:i+2*k]
#         return res