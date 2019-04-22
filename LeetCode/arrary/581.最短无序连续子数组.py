class Solution:
    def findUnsortedSubarray(self,nums):
            # nums: List[int]) -> int:
            i,j = 0 ,len(nums)-1
            tmp = sorted(nums)
            while i<j and nums[i] ==tmp[i]:
                i += 1
            while i<j and nums[j] == tmp[j]:
                j -= 1

            return j-i+1 if i < j else 0


# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         m=nums[0]
#         end=0
#         for i in range(1,len(nums)):
#             if nums[i]>=m:
#                 m=nums[i]
#             else:
#                 end=i
#         m=nums[-1]
#         start=len(nums)-1
#         for i in range(len(nums)-2,-1,-1):
#             if nums[i]<=m:
#                 m=nums[i]
#             else:
#                 start=i
#         if start==end:
#             return 0
#         return max(end-start+1,0)