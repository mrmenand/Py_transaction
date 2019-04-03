# 226. 翻转二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def invertTree(self, root):
#             """DFS"""
#             # root: TreeNode) -> TreeNode:
#             if not root:
#                 return
#             root.left ,root.right = root.right,root.left
#             self.invertTree(root.right)
#             self.invertTree(root.left)
#             return root

class Solution:
    def invertTree(self, root):
        """BFS"""
        if root is None:
            return root
        trees = []
        trees.append(root)
        while trees:
            node = trees.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                trees.append(node.left)
            if node.right:
                trees.append(node.right)
        return root

