# 448. 找到所有数组中消失的数字
class Solution:
    def findDisappearedNumbers(self,nums):
                               # nums: List[int]) -> List[int]:
              return  list(set(range(1,len(nums)+1))-set(nums))

# class Solution:
#     def findDisappearedNumbers(self, nums):
#
#         l = []
#         s = set(nums)
#         for i in range(1, len(nums) + 1):
#             if i not in s:
#                 l.append(i)
#         return l