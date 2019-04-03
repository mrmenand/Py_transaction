# 590.N叉树的后序遍历.py
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


# class Solution:
#     def postorder(self,root):
#             # root: 'Node') -> List[int]:
#             if not root:
#                 return []
#             res =[]
#             for child in root.children:
#                 res += self.postorder(child)
#
#             res.append(root.val)
#
#             return res

class Solution:
    def postorder(self,root):

        if not  root:
            return []
        res = []
        stack = [root]
        while stack :
            node = stack.pop()
            res.append(root.val)
            stack.extend(root.children)
        return res[::-1]