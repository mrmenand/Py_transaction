# 637. 二叉树的层平均值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
            # root: TreeNode) -> List[float]:
            if not root:
                return
            stack= [root]
            res = []
            while stack:
                tmp = []
                n = len(stack)
                for i in range(n):
                    node = stack.pop(0)
                    tmp.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                res.append(sum(tmp)/n)
                
            return res