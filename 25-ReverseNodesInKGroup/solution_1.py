# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        groupPrev = res
        while True:
            groupCurr = groupPrev
            count = 0
            while groupCurr and count < k:
                groupCurr = groupCurr.next
                count += 1
            if not groupCurr:
                break

            groupNext = groupCurr.next

            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = groupCurr
            groupPrev = tmp

        return res.next

