"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev = collections.defaultdict(lambda: Node(0))
        prev[None] = None

        curr = head
        while curr:
            prev[curr].val = curr.val
            prev[curr].next = prev[curr.next]  # curr.next will exist, so we can assign it
            prev[curr].random = prev[curr.random]
            curr = curr.next
        return prev[head]
