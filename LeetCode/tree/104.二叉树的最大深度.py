# 104. 二叉树的最大深度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
                 # root: TreeNode) -> int:
          if not root:
              return 0
          else:
              return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
#上面属于深度优先遍历
#下面输出广度优先遍历

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0  # Check the input parameter
#         else:  # BFS
#             queue = collections.deque()
#             queue.append(root)  # Auxiliary queue
#             maxlevel = 0  # Record level
#             while queue:
#                 levelsize = len(queue)
#                 for i in range(levelsize):
#                     node = queue.popleft()
#                     if node.left:
#                         queue.append(node.left)
#                     if node.right:
#                         queue.append(node.right)
#                 maxlevel += 1
#
#             return maxlevel