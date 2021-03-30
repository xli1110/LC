# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        p1 = headA
        p2 = headB

        while p1 != p2:
            p1 = p1.next if p1 is not None else headB
            p2 = p2.next if p2 is not None else headA
        return p1
