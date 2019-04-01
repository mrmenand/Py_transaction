# 496.下一个更大的元素
class Solution:
    def nextGreaterElement(self,nums1,nums2):
                # nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in range(len(nums2)):
            j = i
            while j < len(nums2)-1:
                if nums2[j+1] > nums2[i]:
                    d[nums2[i]] = nums2[j+1]
                    break
                j += 1

        for i in range(len(nums1)):
            if nums1[i] in d:
                nums1[i] = d[nums1[i]]
            else:
                nums1[i] = -1
        return nums1


# class Solution:
#     def nextGreaterElement(self, nums1, nums2):
#         r = []
#         for i in nums1:
#             for k in nums2[nums2.index(i):]:
#                 if k > i:
#                     r.append(k)
#                     break
#                 if k == nums2[-1]:
#                     r.append(-1)
#         return r


# class Solution:
# #     def nextGreaterElement(self, nums1, nums2):
# #         stack = []   #单调栈
# #         dic = {}   # 字典
# #
# #         # 利用单调栈，将num2中所有值的对应更大元素存入dic
# #         for i in nums2:
# #             while stack and i>stack[-1]:    #此处用while而不是if
# #                 dic[stack.pop()] = i
# #             stack.append(i)
# #
# #         # 遍历num1，根据dic中的记录改写num1
# #         for j in range(len(nums1)):
# #             nums1[j] = dic.get(nums1[j], -1)
# #
# #         return nums1