# 769. 最多能完成排序的块
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ret, max_val = 0, arr[0]
        for i, num in enumerate(arr):
            if num > max_val:
                max_val = num
            if max_val == i:
                ret += 1

        return ret
