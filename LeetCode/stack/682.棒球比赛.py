# 682.棒球比赛
class Solution:
    def calPoints(self, ops):
         #: List[str]) -> int:
         stack = []
         score = 0
         for i in ops:
             if i == "+":
                 a = stack[-2] + stack[-1]
                 stack.append(a)
                 score += (a)
             elif i == "C":
                 score -= stack[-1]
                 stack.pop()
             elif i == "D":
                 a = stack[-1] * 2
                 stack.append(a)
                 score += a
             else:
                 stack.append(int(i))
                 score += int(i)

         return score

tset = Solution()
print(tset.calPoints(ops=["5","2","C","D","+"]))

