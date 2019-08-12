# 26. 删除排序数组中的重复项

class Solution:
    def removeDuplicates(self,nums):
            # nums: List[int]) -> int
        if not nums:
            return 0
        i = 1
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
        return i



# test = Solution()
# print(test.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))
