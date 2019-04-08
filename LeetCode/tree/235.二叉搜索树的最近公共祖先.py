#235 二叉搜索数的最最近公共祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self,root,p,q):
           # root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
           if max(p.val,q.val) < root.val:
               return self.lowestCommonAncestor(root.left,p,q)
           if min(p.val,q.val) > root.val:
               return self.lowestCommonAncestor(root.right,p,q)
           return root
