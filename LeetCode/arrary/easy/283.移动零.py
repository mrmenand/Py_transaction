# 283.移动零

class Solution:
    def moveZeroes(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

# class Solution:
#     def moveZeroes(self, nums):
#          # nums: List[int]) -> None:
#          for  i in nums:
#              if i ==0:  ## 虽然用removl 比较简单，但是不好
#                  nums.insert(len(nums),i)
#                  nums.pop(nums.index(i))




