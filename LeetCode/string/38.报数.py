# 38. 报数
class Solution:
    def countAndSay(self,n):
            # n: int) -> str:
           s = "1"
           for i in range(1,n):
               length = 1
               result = ""
               for j in range(len(s)):
                   if j < len(s)-1 and s[j] == s[j+1]:
                       length += 1
                   else:
                       result  += str(length)+ s[j]
                       length = 1

               s = result

           return  s


