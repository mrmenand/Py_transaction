# 572. 另一个树的子树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self,s,t):
          # s: TreeNode, t: TreeNode) -> bool:
         stack = [s]
         while stack:
             node = stack.pop()
             if self.same(node,t):
                 return True
             if node.left:
                 stack.append(node.left)
             if node.right:
                 stack.append(node.right)
         return False

    def same(self,s,t):
        if not s  and not t:
            return True
        elif s and t and s.val == t.val:
            return self.same(s.left,t.left) and self.same(s.right,t.right)
        else:
            return False

