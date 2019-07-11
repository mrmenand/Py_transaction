# 1013. 将数组分成和相等的三个部分
from collections import deque


class Solution:
    def canThreePartsEqualSum(self,A):
             # A: List[int]) -> bool:
             avg = sum(A)//3
             if  sum(A)%3 != 0:
                 return False

             i = 0
             j = len(A)-1
             left,right = 0,0
             res = False
             while i < j:
                 if left != avg:
                     left += A[i]
                     i += 1

                 if right != avg:
                     right += A[j]
                     j -= 1

                 if left ==avg == right:
                     res = True
                     break

             return res



