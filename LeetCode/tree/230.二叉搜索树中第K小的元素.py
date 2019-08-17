# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        val = self.yield_tree(root)
        for _ in range(k - 1):
            next(val)
        return next(val)

    def yield_tree(self, node):
        # 中序遍历
        # if node.left:
        #     for i in self.yield_tree(node.left):
        #         yield i
        # yield from常用来代替内层for循环 与 打开双通道
        if node.left:
            yield from self.yield_tree(node.left)
        yield node.val
        if node.right:
            for i in self.yield_tree(node.right):
                yield i

# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#
#         ret = []
#         self.inorder(root,ret)
#         return ret[k-1]
#
#     def inorder(self,node,ret):
#         if not node:
#             return
#         self.inorder(node.left,ret)
#         ret.append(node.val)
#         self.inorder(node.right,ret)
