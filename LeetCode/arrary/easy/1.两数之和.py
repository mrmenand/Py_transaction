# 1.两数之和
class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for index,num in enumerate(nums):
            a = target - num
            if a in dic:
                return [dic[a],index]
            dic[num] = index
        return None


# class Solution:
#     def twoSum(self, nums,target):
#                # nums: List[int], target: int) -> List[int]:
#                for i in range(len(nums)):
#                    if target - nums[i] in nums[i + 1:]:
#                        sec_ind = nums[i + 1:].index(target - nums[i]) + i + 1
#                        return [i , sec_ind]

