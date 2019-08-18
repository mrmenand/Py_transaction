# 969. 煎饼排序
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ret, n = [], len(A)
        while n:
            idx = A.index(n)
            ret.append(idx + 1)
            A = A[:idx + 1][::-1] + A[idx + 1:]
            ret.append(n)
            A = A[:n][::-1] + A[n:]
            n -= 1

        return ret
