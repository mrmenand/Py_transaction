# 112. 路径总和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self,root,sum):
            # root: TreeNode, sum: int) -> bool:
            if not root:
                return False
            sum -= root.val
            if not root.left and not  root.right:
                return sum == 0
            else:
                return self.hasPathSum(root.left) or self.hasPathSum(root.right)