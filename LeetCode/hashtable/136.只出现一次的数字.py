# 136. 只出现一次的数字
class Solution(object):
    def singleNumber(self, nums):
        i = 0
        for num in nums:
            i = i ^ num

        return i

