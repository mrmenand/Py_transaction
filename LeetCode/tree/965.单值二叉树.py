# 965. 单值二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isUnivalTree(self, root):
#          # root: TreeNode) -> bool:
#         if not root:
#             return True
#         if root.left:
#             if root.left.val != root.val:
#                 return False
#
#         if root.right:
#             if root.right.val != root.val:
#                 return False
#
#         if self.isUnivalTree(root.left) and self.isUnivalTree(root.right):
#             return True
#         else:
#             return False
#

class Solution:
    def isUnivalTree(self, root):
        stack = [root]
        flag = root.val

        while stack:
            node = stack.pop()
            if node.val != flag:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return True




