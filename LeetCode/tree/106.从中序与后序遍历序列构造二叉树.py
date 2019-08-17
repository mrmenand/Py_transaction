# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.left = self.buildTree(inorder[:idx],postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:],postorder[idx:])

        return root

