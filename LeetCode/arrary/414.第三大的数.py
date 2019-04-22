# 414. 第三大的数
class Solution:
    def thirdMax(self,nums):
            # nums: List[int]) -> int:
            first,second,third = float("-inf"),float("-inf"),float("-inf")
            for num in nums:
                if num > first:
                    first, second, third = num, first, second
                elif second < num < first:
                    second, third = num, second
                elif third < num < second:
                    third = num

            return third if third != float("-inf") else  first