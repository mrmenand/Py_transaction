# 404. 左叶子之和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self,root):
            # root: TreeNode) -> int:
            if not root:
                return 0
            stack = [root]
            left = []
            while stack:
                 node = stack.pop()
                 if node.left:
                     stack.append(node.left)
                     if not node.left.left  and not node.left.right:
                         left.append(node.left.val)
                 if node.right:
                     stack.append(node.right)

            return sum(i for i in left)

# class Solution:
#     def sumOfLeftLeaves(self,root):
#         if not root:
#             return 0
#         if root.left and not root.left.left and not root.left.right:
#             return root.left.val + self.sumOfLeftLeaves(root.right)
#         else:
#             return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


