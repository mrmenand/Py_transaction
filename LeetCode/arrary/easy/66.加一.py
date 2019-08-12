class Solution:
    def plusOne(self,digits):
            # digits: List[int]) -> List[int]:
            #  num = int("".join(str(num) for num in digits))+1
            #  return [int(i) for i in str(num)]
            return   [int(i) for i in (str(int("".join(str(num) for num in digits))+1))]