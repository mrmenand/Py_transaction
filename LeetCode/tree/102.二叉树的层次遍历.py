# 102.二叉树的层次遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret

        def _dfs(root, depth):
            if root:
                if depth + 1 > len(ret):
                    ret.append([])
                ret[depth].append(root.val)
                _dfs(root.left, depth + 1)
                _dfs(root.right, depth + 1)

        _dfs(root, 0)
        return ret

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         stack = [root]
#         ret = []
#
#         while stack:
#             tmp = []
#             for i in range(len(stack)):
#                 node = stack.pop(0)
#                 tmp.append(node.val)
#                 if node.left:
#                     stack.append(node.left)
#                 if node.right:
#                     stack.append(node.right)
#             ret.append(tmp)
#
#         return ret
