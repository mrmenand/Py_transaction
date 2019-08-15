#561.数组拆分
class Solution:
    def arrayPairSum(self,nums):
        # nums: List[int]) -> int
        nums.sort()
        sum_min=0
        for i in range(0,len(nums),2):
            sum_min +=min(nums[i],nums[i+1])

        return sum_min

nums = [1,4,3,2]
test = Solution()
print(test.arrayPairSum(nums))

# class Solution:
#     def arrayPairSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort&search()
#         sum=0
#         for i in nums[::2]:
#             sum=sum+i
#         return sum


