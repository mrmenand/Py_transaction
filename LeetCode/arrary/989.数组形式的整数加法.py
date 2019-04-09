# 989. 数组形式的整数加法
class Solution:
    def addToArrayForm(self, A,K):
            # A: List[int], K: int) -> List[int]:
        # a = 0
        # for i in range(len(A)):
        #     a += A[i]*10**(len(A)-1-i)
        a = "".join([str(i) for i in A])
        a = int(a)
        b = a + K
        return [int(j) for j in str(b)]