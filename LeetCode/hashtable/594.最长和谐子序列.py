# 594. 最长和谐子序列
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:

        res = 0
        hashmap = Counter(nums)
        # hashmap = {}
        # for i in nums:
        #     if i not in hashmap:
        #         hashmap[i] = 0
        #     hashmap[i] += 1
        # hashmap = sorted(hashmap.items(), key= lambda x: x[1], reverse= True)
        # print(hashmap)

        for num in nums:
            if num + 1 in hashmap:
                res = max(res,hashmap[num] + hashmap[num+1])
        
        return res
                

