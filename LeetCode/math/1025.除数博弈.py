# 1025. 除数博弈
## 智力题 谁之后拿最后一个一，谁就赢
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
