# 107. 二叉树的层次遍历 II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self,root):
                # root: TreeNode) -> List[List[int]]:
           if not root:
               return []
           stack = [root]
           res = []
           while stack:
                tmp = []
                for i in range(len(stack)):
                    node = stack.pop(0)
                    tmp.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                res.append(tmp)

           return res[::-1]

