# 700. 二叉搜索树中的搜索
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root,val):
         # root: TreeNode, val: int) -> TreeNode:
         if not root:
             return
         if val == root.val:
             return root
         elif val < root.val:
             return self.searchBST(root.left,val)
         else:
             return self.searchBST(root.right,val)