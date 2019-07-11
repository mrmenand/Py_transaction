# 509. 斐波那契数
class Solution:
    def fib(self,N):
        # N: int) -> int
        if N==0:
            return 0
        elif N==1:
            return 1
        else:
            return self.fib(N-1)+self.fib(N-2)

# class Solution:
#     def fib(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         cache = {}
#         def recur_fib(N):
#             if N in cache:
#                 return cache[N]
#
#             if N < 2:
#                 result = N
#             else:
#                 result = recur_fib(N-1) + recur_fib(N-2)
#
#             # put result in cache for later reference.
#             cache[N] = result
#             return result
#
#         return recur_fib(N)