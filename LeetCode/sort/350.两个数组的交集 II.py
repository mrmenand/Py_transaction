# 350. 两个数组的交集 II
class Solution:
    def intersect(self, nums1,nums2):
                  # nums1: List[int], nums2: List[int]) -> List[int]:
                 intersection = set(nums1) & set(nums2)
                 res = []
                 for i in intersection:
                      res += [i] * min(nums1.count(i),nums2.count(i))

                 return res

# class Solution:
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         from collections import Counter
#         return list((Counter(nums1) & Counter(nums2)).elements())