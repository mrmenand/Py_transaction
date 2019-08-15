# 53. 最大子序和

class Solution:
    def maxSubArray(self, nums):
        status = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] + status[i-1] > nums[i] :
                status.append(nums[i] + status[i-1])

            else:
                status.append(nums[i])

        return max(status)

# class Solution:
#     def maxSubArray(self, nums):
#             # nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和
#             for i in range(1,len(nums)):
#                 nums[i] = nums[i] +max(nums[i-1],0)
#
#             return max(nums)
