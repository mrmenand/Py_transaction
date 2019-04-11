# 606. 根据二叉树创建字符串
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t):
          # t: TreeNode) -> str:
          if not t:
              return ""

          s = str(t.val)
          left = self.tree2str(t.left)
          right = self.tree2str(t.right)

          if  left == "" and right == "":
              return s
          elif left =="":
              s += "()"+"("+right+")"
          elif right =="":
              s += "("+left+")"
          else:
              s += "("+left+")"+"("+right+")"

          return s


# class Solution:
#     def tree2str(self, t: 'TreeNode') -> 'str':
#
#         if t == None:
#             return ""
#         s = str(t.val)
#         if t.left:
#             s += '(' + self.tree2str(t.left) + ')'
#         if t.right:
#             if not t.left:
#                 s += '()'
#             s += '(' + self.tree2str(t.right) + ')'
#         return s
