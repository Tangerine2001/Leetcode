# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head

        while True:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False

            if not slow or not fast:
                return False

            if slow == fast:
                return True
        return False