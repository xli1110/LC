# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = {}
        p = head
        while p is not None:
            d[p] = Node(p.val)
            p = p.next

        p = head
        while p is not None:
            d[p].next = d.get(p.next, None)
            d[p].random = d.get(p.random, None)
            p = p.next

        return d.get(head, None)
