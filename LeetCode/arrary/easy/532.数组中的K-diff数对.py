# 532. 数组中的K-diff数对
class Solution:
    def findPairs(self,nums,k):
            # nums: List[int], k: int) -> int:
            cnt = 0
            tmp = {}
            if k < 0:
                return 0
            for i in nums:
                if i in tmp.keys():
                    tmp[i] += 1
                else:
                    tmp[i] = 1

            for key,v in tmp.items():
                if k == 0:
                    if v >= 2:
                        cnt += 1
                elif key + k in tmp.keys():
                    cnt += 1

            return cnt





