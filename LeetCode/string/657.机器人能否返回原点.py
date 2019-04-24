# 657. 机器人能否返回原点
class Solution:
    def judgeCircle(self,moves):
            # moves: str) -> bool:
            return moves.count("R") == moves.count("L") and moves.count("D") == moves.count("U")

