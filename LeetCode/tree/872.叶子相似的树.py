# 872. 叶子相似的树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self,root1,root2):
            # root1: TreeNode, root2: TreeNode) -> bool:
            return self.getleaf(root1) == self.getleaf(root2)


    def getleaf(self,root):
        if not root:
            return []
        stack = [root]
        leaf = []
        while stack:
           node = stack.pop()
           if not node.left and not node.right:
              leaf.append(node.val)
           if node.left:
               stack.append(node.left)
           if node.right:
               stack.append(node.right)


        return leaf



