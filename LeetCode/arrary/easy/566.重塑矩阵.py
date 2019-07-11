# 566. 重塑矩阵
class Solution:
    def matrixReshape(self, nums,r,c):
          # nums: List[List[int]], r: int, c: int) -> List[List[int]]:
          row = len(nums)
          column = len(nums[0])
          res = []
          ori = []
          for i in nums:
              ori +=i   ##二维列表拼接成一维列表
          if row * column == r*c:
              for i in range(r):
                  res.append(ori[c*i:c*(i+1)])
              return res

          else:
              return nums


# class Solution:
#     def matrixReshape(self, nums, r, c):
#         """
#         :type nums: List[List[int]]
#         :type r: int
#         :type c: int
#         :rtype: List[List[int]]
#         """
#         rows = len(nums)
#         if rows == 0:
#             return []
#         cols = len(nums[0])
#         if (r * c) != (rows * cols):
#             return nums
#         new_nums = []
#         for i in range(rows):
#             for j in range(cols):
#                 new_nums.append(nums[i][j])
#         return[new_nums[i*c:(i+1)*c] for i in range(r)]