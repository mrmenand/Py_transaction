# 667. 优美的排列 II
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ret = [i for i in range(1,n+1)]
        for i in range(1,k):
            ret[i:] = ret[i:][::-1]

        return ret