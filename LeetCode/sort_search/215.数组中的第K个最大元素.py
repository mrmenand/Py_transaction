# 215. 数组中的第K个最大元素
import heapq
import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left,right,pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index],nums[right] = nums[right],nums[pivot_index]

            store_left = left
            for i in range(left,right):
                if nums[i] < pivot:
                    nums[store_left],nums[i] = nums[i],nums[store_left]
                    store_left += 1

            nums[right],nums[store_left] = nums[store_left],nums[right]

            return store_left

        def select(left,right,k_smallest):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left,right)
            pivot_index = partition(left,right,pivot_index)

            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left,pivot_index-1,k_smallest)
            else:
                return select(pivot_index+1,right,k_smallest)

        return select(0,len(nums)-1,len(nums)-k)










# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap_min = []
#         for num in nums[:k]:
#             heapq.heappush(heap_min,num)
#
#         for num in nums[k:]:
#             if num > heap_min[0]:
#                 heapq.heappop(heap_min)
#                 heapq.heappush(heap_min,num)
#
#         return heap_min[0]

a = Solution()
print(a.findKthLargest(nums=[3,2,1,5,6,4],k=2))
