# 169. 求众数
from collections import Counter
class Solution:
    def majorityElement(self, nums):
            # nums: List[int]) -> int:
            max = Counter(nums).most_common(1)
            # print(max[0][0])
            if max[0][1]>(len(nums)/2):
                return max[0][0]

test = Solution()
print(test.majorityElement(nums=[2,2,1,1,1,2,2]))


# class Solution:
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort&search()
#         n = int(len(nums)/2)
#         return nums[n]