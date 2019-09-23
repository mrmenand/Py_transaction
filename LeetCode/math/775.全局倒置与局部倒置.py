# 775. 全局倒置与局部倒置
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if abs(A[i] - i) >= 2 :
                return False

        return True
