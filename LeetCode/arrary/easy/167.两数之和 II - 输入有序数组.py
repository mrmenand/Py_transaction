# 167. 两数之和 II - 输入有序数组
# class Solution:  #超时
#     def twoSum(self,numbers,target):
#                # numbers: List[int], target: int) -> List[int]:
#           for i in range(len(numbers)):
#               for j in range(i+1,len(numbers)):
#                   if numbers[i] + numbers[j] ==target:
#                       return [i+1,j+1]

class Solution:
    def twoSum(self,numbers,target):
        for i in range(len(numbers)):
            if target-numbers[i] in numbers[i+1:]:
                sec_ind = numbers[i+1:].index(target-numbers[i])+i+1
                return [i+1,sec_ind+1]


# class Solution:
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         i = 0
#         j = len(numbers)-1
#         while i < j:
#             if numbers[i]+numbers[j]>target:
#                 j -= 1
#             elif numbers[i]+numbers[j]<target:
#                 i += 1
#             else:
#                 return [i+1,j+1]
#         return []
