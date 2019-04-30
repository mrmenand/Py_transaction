# 234. 回文链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next

        return stack == stack[::-1]

