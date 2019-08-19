# 347. 前 K 个高频元素
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_max = []
        dic = {}
        ret = []
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        for i in dic:
            heapq.heappush(heap_max,(-dic[i],i))

        for i in range(k):
            ret.append(heapq.heappop(heap_max)[1])


        return ret






# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dic = {}
#         for i in nums:
#             dic[i] = dic.get(i, 0) + 1
#         match = sorted(dic.items(), key=lambda x: x[1])
#         ret = []
#         for i in range(1, k + 1):
#             ret.append(match[-i][0])
#
#         return ret
