class Solution:
    def plusOne(self,digits):
            # digits: List[int]) -> List[int]:
             num = int("".join(str(num) for num in digits))+1
             return [i for i in num]