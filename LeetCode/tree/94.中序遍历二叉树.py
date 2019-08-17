# 94.中序遍历二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        while root:
            ret += self.inorderTraversal(root.left)
            ret.append(root.val)
            ret += self.inorderTraversal(root.right)

        return ret 


# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#
#         ret,stack = [],[]
#         while 1:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             if not stack:
#                 return ret
#             node = stack.pop()
#             ret.append(node.val)
#             root = node.right
#
#         return ret











