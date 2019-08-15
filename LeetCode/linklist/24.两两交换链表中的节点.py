# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        tmp = head.next
        head.next = self.swapPairs1(head.next.next)
        tmp.next = head
        return tmp

    def swapPairs2(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        h = head

        while h:
            if h and h.next:
                tmp = h.next
                p.next = tmp
                h.next = h.next.next
                tmp.next = h

                h = h.next
                p = p.next.next
            else:
                p.next = h
                h = h.next

        return dummy.next
