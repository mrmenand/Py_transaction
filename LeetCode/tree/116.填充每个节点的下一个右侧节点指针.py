# 116. 填充每个节点的下一个右侧节点指针
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if root.left:
            root.left.next = root.right # 亲兄弟
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

        return root


# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:
#             return None
#         stack = [root]
#         while stack :
#             node_pre = None
#             for _ in range(len(stack)):
#                 node = stack.pop(0)
#                 if node_pre:
#                     node_pre.next = node
#                 node_pre = node
#                 if node.left or node.right:
#                     stack.append(node.left)
#                     stack.append(node.right)
#         return root
#


