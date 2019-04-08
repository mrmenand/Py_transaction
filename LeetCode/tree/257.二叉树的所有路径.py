# 257. 二叉树的所有路径
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self,root):
            # root: TreeNode) -> List[str]:
            if not root:
                return []
            paths = []
            if not root.left and not root.right:
                return [str(root.val)]
            if root.left:
                for i in self.binaryTreePaths(root.left):
                    paths.append(str(root.val)+"->"+i)
            if root.right:
                for i in self.binaryTreePaths(root.right):
                    paths.append(str(root.val)+"->"+i)
            return paths