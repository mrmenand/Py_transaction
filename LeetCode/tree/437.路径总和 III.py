# 437. 路径总和 III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = 0
    def pathSum(self, root,sum):
        # root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.NodePath(root,sum)
        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)
        return self.result


    def  NodePath(self,root,sum):
        if not  root:
            return
        sum -= root.val
        if sum == 0 :
            self.result += 1
        self.NodePath(root.left,sum)
        self.NodePath(root.right,sum)