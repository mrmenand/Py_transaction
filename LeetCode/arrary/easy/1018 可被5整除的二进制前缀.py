# 1018. 可被 5 整除的二进制前缀
class Solution:
    def prefixesDivBy5(self,A):
            # A: List[int]) -> List[bool]:
            num ,res = 0, []
            for i in A:
                num = num * 2 +i
                res.append(num)
            return [num % 5 ==0 for num in res]

# class Solution:
#     def prefixesDivBy5(self, A: List[int]) -> List[bool]:
#         N = []
#         pref = 0
#         for a in A:
#             pref = (pref*2+a)%5
#             N.append(not pref)
#         return N