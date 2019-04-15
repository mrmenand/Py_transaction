# 110. 平衡二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
            # root: TreeNode) -> bool:
            if not root:
                return True
            print(self.maxDepth(root.left))
            print(self.maxDepth(root.right))
            print("nishidid")
            if abs(self.maxDepth(root.left)-self.maxDepth(root.right)) >1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalance(root.right)


    def maxDepth(self,root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
