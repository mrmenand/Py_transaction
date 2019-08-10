# 79. 第K个语法符号
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:

        if N == 1:
            return 0
        ret = self.kthGrammar(N-1,(K+1)//2)

        if ret :
            return 0 if  K % 2 == 0 else 1
        else :
            return 1 if K % 2 == 0 else  0

