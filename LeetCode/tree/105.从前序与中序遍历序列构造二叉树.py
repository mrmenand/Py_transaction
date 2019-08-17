# 105. 从前序与中序遍历序列构造二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])

        return root