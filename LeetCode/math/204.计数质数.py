# 204. 计数质数
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        prime = [1] * n
        prime[0], prime[1] = 0, 0
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                prime[i * i:n:i] = [0] * len(prime[i * i:n:i])

        return sum(prime)


