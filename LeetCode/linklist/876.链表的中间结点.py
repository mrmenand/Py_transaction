# 876. 链表的中间结点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow