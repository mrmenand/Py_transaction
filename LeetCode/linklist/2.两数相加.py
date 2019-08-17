# 2.两数相加
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        ret = dummy
        carry = 0  # 进位
        while l1 or l2:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            sum = x1 + x2 + carry
            carry = sum // 10
            ret.next = ListNode(sum%10)
            ret = ret.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            ret.next = ListNode(1)

        return dummy.next
