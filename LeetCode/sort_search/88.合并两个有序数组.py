# 88.合并两个有序数组.py
class Solution:
    def merge(self, nums1, m, nums2, n):
        i, j = m - 1, n - 1
        for k in range(m + n - 1, -1, -1):
            if i == -1:
                nums1[k] = nums2[j]
                j -= 1
            elif j == -1:
                break
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         nums3 = nums1[:m]
#         i, j = 0, 0
#         for k in range(m + n):
#             if i == m:
#                 nums1[k] = nums2[j]
#                 j += 1
#             elif j == n:
#                 nums1[k] = nums3[i]
#                 i += 1
#             elif nums3[i] < nums2[j]:
#                 nums1[k] = nums3[i]
#                 i += 1
#             else:
#                 nums1[k] = nums2[j]
#                 j += 1

# class Solution:
#     def merge(self, nums1,m,nums2,n):
#             # nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#             nums1[m:m+n] = nums2
#             nums1.sort_search()
