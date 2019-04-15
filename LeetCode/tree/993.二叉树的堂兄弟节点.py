# 993. 二叉树的堂兄弟节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self,root,x,y):
            # root: TreeNode, x: int, y: int) -> bool:
            if not root:
                return False
            stack = [root]

            while stack:
                tmp = []
                x_parent,y_parent = None,None
                for node in stack:
                    if node.left:
                        tmp.append(node.left)
                        if node.left.val == x:
                            x_parent = node
                        if node.left.val == y:
                            y_parent = node

                    if node.right:
                        tmp.append(node.right)
                        if node.right.val == x:
                            x_parent = node
                        if node.right.val == y:
                            y_parent = node

                stack = tmp

                if x_parent and y_parent and x_parent != y_parent:
                    return True

            return False








