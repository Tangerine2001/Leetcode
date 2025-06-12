# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode(0, None)
        curr = res
        while l1 and l2:
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            curr.next = ListNode(digit, None)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            carry, digit = divmod(l1.val + carry, 10)
            curr.next = ListNode(digit, None)
            curr = curr.next
            l1 = l1.next

        while l2:
            carry, digit = divmod(l2.val + carry, 10)
            curr.next = ListNode(digit, None)
            curr = curr.next
            l2 = l2.next

        if carry:
            curr.next = ListNode(carry, None)

        return res.next
