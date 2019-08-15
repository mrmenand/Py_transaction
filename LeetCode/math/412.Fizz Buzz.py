# 412 Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["Fuzz"*(not i % 3 ) + "Buzz"*(not i % 5) or str(i)  for i in range(1,n+1)]
