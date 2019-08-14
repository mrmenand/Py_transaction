# 101.对称二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetric(self, root):
        def match(l,r):
            if not l and not r :
                return True
            if not l or not r :
                return False
            return l.val == r.val and match(l.left,r.right) and match(l.right,r.left)

        return match(root,root)


# class Solution:
#     def isSymmetric(self, root):
#         # root: TreeNode) -> bool:
#         if not root:
#             return True
#         stack = [root]
#
#         while stack:
#             tmp = []
#             for i in range(len(stack)):
#                 node = stack.pop(0)
#                 if node:
#                     tmp.append(node.val)
#                     if node.left:
#                         stack.append(node.left)
#                     else:
#                         stack.append(None)
#                     if node.right:
#                         stack.append(node.right)
#                     else:
#                         stack.append(None)
#                 else:
#                     tmp.append("*")
#             print(tmp)
#
#             if tmp != tmp[::-1]:
#                 return False
#
#         return True

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#
#         hander = [[root.left, root.right]]
#
#         while len(hander):
#             node1, node2 = hander.pop(0)
#
#             if not node1 and not node2:
#                 pass
#             elif not node1 or not node2:
#                 return False
#             elif node1.val == node2.val:
#                 hander.insert(0, [node1.left, node2.right])
#                 hander.insert(0, [node1.right, node2.left])
#             else:
#                 return False
#         return True


# class Solution:
#     def isSymmetric(self, root: 'TreeNode') -> 'bool':
#         if not root:
#             return True
#         else:
#             return self.isNodeEqual(root.left, root.right)
# 
#     def isNodeEqual(self, l, r):
#         if not l and not r:
#             return True
#         elif not l or not r or l.val != r.val:
#             return False
#         else:
#             return self.isNodeEqual(l.left, r.right) and self.isNodeEqual(l.right, r.left)
