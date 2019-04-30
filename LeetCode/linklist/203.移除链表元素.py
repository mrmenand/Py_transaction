# 203. 移除链表元素
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        pre = ListNode(None)
        pre.next = head
        node = pre
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return pre.next



