# 429. N叉树的层序遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
         # root: 'Node') -> List[List[int]]:
         if not root:
             return []
         stack = [root]
         res = []
         while stack:
             temp = []
             for  i in range(len(stack)):
                 node = stack.pop(0)
                 temp.append(node.val)
                 for child in node.children:
                     stack.append(child)

             res.append(temp)

         return res




