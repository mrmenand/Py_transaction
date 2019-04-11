# 653. 两数之和 IV - 输入 BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
       self.nums = []

    def findTarget(self,root,k):
            # root: TreeNode, k: int) -> bool:
            if not root:
                return False
            self.inorder(root)
            print(self.nums)

            low,high = 0,len(self.nums)-1
            while low < high:
                if self.nums[low] + self.nums[high] ==k:
                    return True
                elif self.nums[low] + self.nums[high] > k:
                    high -= 1
                elif self.nums[low] + self.nums[high] < k:
                    low  += 1

            return False


    def inorder(self,root):
        if not root:
            return []
        self.inorder(root.left)
        self.nums.append(root.val)
        self.inorder(root.right)


# class Solution:
#     def findTarget(self, root: TreeNode, k: int) -> bool:
#         if not root:
#             return False
#
#         queue = [root]
#         nums = set()
#         for node in queue:
#             val = node.val
#             if k - val in nums:
#                 return True
#             nums.add(val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#         return False

