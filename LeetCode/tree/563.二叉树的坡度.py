# 563. 二叉树的坡度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self,root):
         # root: TreeNode) -> int:
         nsum,tilt = self.dfs(root)
         return tilt
    def dfs(self,root):
         if not root:
             return 0,0
         lsum,ltilt = self.dfs(root.left)
         rsum,rtilt = self.dfs(root.right)
         return  lsum+rsum+root.val,ltilt+rtilt+abs(lsum-rsum)


