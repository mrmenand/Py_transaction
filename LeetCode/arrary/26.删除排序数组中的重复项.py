# 26. 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self,nums):
            # nums: List[int]) -> int
            if not nums:
                return 0
            j = 0
            for i in range(len(nums)-1):
                if nums[i] != nums[i+1]:
                   nums[j] = nums[i]
                   j += 1
            nums[j] = nums[len(nums)-1]
            # print(nums)

            return j+1


# test = Solution()
# print(test.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))
