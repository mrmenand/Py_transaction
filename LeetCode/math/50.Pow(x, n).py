# 50.Pow(x,n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                return helper(x * x, n // 2)
            return helper(x * x, (n - 1) // 2) * x

        if n < 0 :
            n = -n
            return 1/helper(x,n)
        return helper(x,n)








        def myPow(self, x: float, n: int) -> float:
            if n < 0:
                x = 1 / x
                n = -n

            if n == 0:
                return 1
            if n == 1:
                return x

            if n % 2 == 0:
                return self.myPow(x, n / 2) ** 2
            else:
                return self.myPow(x, n - 1) * x

            class Solution(object):
                def myPow(self, x, n):
                    """
                    :type x: float
                    :type n: int
                    :rtype: float
                    """
                    i = n
                    if i < 0: i = -i
                    res = 1
                    while i != 0:
                        if i % 2 != 0: res *= x
                        x *= x
                        i = i // 2
                    return res if n > 0 else 1 / res
