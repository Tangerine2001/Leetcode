# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # right is head.next to ensure the slow is always
        # at least one left of middle
        # this makes it easy to reverse the right side
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the right side
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # reorder in place
        curr = head
        while prev:
            tempCurr, tempNext = curr.next, prev.next
            curr.next = prev
            prev.next = tempCurr
            curr, prev = tempCurr, tempNext
