def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


class Solution:

    @memo
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N - 1) + self.fib(N - 2)



