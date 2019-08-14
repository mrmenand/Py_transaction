# 98.验证二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(node,min_val,max_val):
            if not node:
                return True

            if node.val >= max_val or node.val <= min_val:
                return False

            return isBST(node.left,min_val,node.val) and isBST(node.right,node.val,max_val)

        return isBST(root,float("-inf"),float("inf"))


# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#
#         if not root:
#             return True
#         num = float("-inf")
#         for i in self.yield_tree(root):
#             if num >=i :
#                 return False
#             num = i
#         return True
#
#     def yield_tree(self,node):
#         # 中序遍历
#         if node.left:
#             for i in self.yield_tree(node.left):
#                 yield i
#         yield node.val
#         if node.right:
#             for i in self.yield_tree(node.right):
#                 yield i
#






