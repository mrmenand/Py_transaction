# # 103. 二叉树的锯齿形层次遍历
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret

        def helper(node, depth):
            if node:
                if depth == len(ret):
                    ret.append([])
                if depth % 2 == 0:
                    ret[depth].append(node.val)
                else:
                    ret[depth].insert(0, node.val)
                helper(node.left, depth + 1)
                helper(node.right, depth + 1)

        helper(root, 0)
        return ret

# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         stack = [root]
#         ret,flag = [],1
#
#         while stack:
#             tmp = []
#             for i in range(len(stack)):
#                 node = stack.pop(0)
#                 if node.left:
#                     stack.append(node.left)
#                 if node.right:
#                     stack.append(node.right)
#                 tmp.append(node.val)
#             if flag == -1:
#                 tmp = tmp[::-1]
#             ret.append(tmp)
#             flag *= -1
#         return ret
#
#
#
