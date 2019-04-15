# 543. 二叉树的直径
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
         # : TreeNode) -> int:
         def maxDepth(root):
             if not root:
                 return 0

             return 1 + max(maxDepth(root.left), maxDepth(root.right))

         if not root:
             return 0
         res = maxDepth(root.left) + maxDepth(root.right)
         res = max(res,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

         return res


