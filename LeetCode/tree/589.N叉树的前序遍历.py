# 589.N叉树的前序遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.res = []

    def preorder(self, root):
            # root: 'Node') -> List[int]:
            if not root:
                return []
            self.res.append(root.val)
            for child in root.children:
                self.preorder(child)

            return self.res


# class Solution(object):
#     def preorder(self, root):
#
#         if not root:
#             return []
#         s = [root]
#         # s.append(root)
#         res = []
#         while s:
#             node = s.pop()
#             res.append(node.val)
#             s.extend(node.children[::-1])
#         return res