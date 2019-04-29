# 686. 重复叠加字符串匹配
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
         if len(set(A)) < len(set(B)):
             return -1
         i = 1
         while len(A*i) <len(A+A+B):
             if B in A*i:
                 return i
             i += 1

         return -1
