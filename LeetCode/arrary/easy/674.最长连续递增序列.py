#674.最长连续递增序列
class Solution:
    def findLengthOfLCIS(self,nums):
            # nums: List[int]) -> int:
            if not nums:
                return 0
            cnt = 1
            max_cnt =1
            for i in range(1,len(nums)):
                if nums[i] > nums[i-1]:
                    cnt += 1
                else:
                    max_cnt = max(cnt,max_cnt)
                    cnt = 1

            max_cnt = max(cnt,max_cnt)
            return max_cnt

