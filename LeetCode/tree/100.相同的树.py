# 100. 相同的树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p,q):
        # p: TreeNode, q: TreeNode) -> bool:
        if not q and not p:
            return True
        elif not q or not p:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True
#         elif not p or not q:
#             return False
#
#         stack = [[p, q]]
#
#         while len(stack):
#             pair = stack.pop()
#             node1, node2 = pair
#             if not node1.val == node2.val: return False
#             if node1.left and node2.left:
#                 stack.append([node1.left, node2.left])
#             elif node1.left or node2.left:
#                 return False
#             if node1.right and node2.right:
#                 stack.append([node1.right, node2.right])
#             elif node1.right or node2.right:
#                 return False
#         return True

##对bool类型进行异或操作
# class Solution:
#
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True
#         if (not p)^(not q):
#             return False
#         if p.val != q.val:
#               return False
#         else:
#             return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)