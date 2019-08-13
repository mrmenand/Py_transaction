# 350. 两个数组的交集 II
# class Solution:
#     def intersect(self, nums1,nums2):
#                   # nums1: List[int], nums2: List[int]) -> List[int]:
#                  intersection = set(nums1) & set(nums2)
#                  res = []
#                  for i in intersection:
#                       res += [i] * min(nums1.count(i),nums2.count(i))
#
#                  return res

class Solution:
    def intersect(self, nums1, nums2):

        dic,ret = {},[]
        for  i in nums1:
            dic[i] = dic.get(i,0) + 1
        for i in nums2:
            dic[i] = dic.get(i, 0)
            if dic[i] != 0 :
                ret.append(i)
                dic[i] -= 1
        return ret



