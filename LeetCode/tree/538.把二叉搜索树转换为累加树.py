# 538. 把二叉搜索树转换为累加树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.s_val = 0
    def convertBST(self,root):
            # root: TreeNode) -> TreeNode:
            if not root:
                return
            self.convertBST(root.right)
            # print(self.s_val)
            self.s_val += root.val
            print(self.s_val)
            root.val = self.s_val
            self.convertBST(root.left)
            return root


            # stack = [root]
            # while stack:
            #     node = stack.pop()
            #     if node
