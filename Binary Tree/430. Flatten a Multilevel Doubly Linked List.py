# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head

        while p is not None:
            if p.child is None:
                p = p.next
            else:
                t = p
                

        return head
