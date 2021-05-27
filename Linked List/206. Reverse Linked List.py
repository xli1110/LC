# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1 = None
        p2 = head

        while p2 is not None:
            temp1 = p1
            temp2 = p2
            p1 = temp2  # Note we can NOT use p1 = p1.next, since p1 is None at initialization.
            p2 = temp2.next
            temp2.next = temp1

        return p1
