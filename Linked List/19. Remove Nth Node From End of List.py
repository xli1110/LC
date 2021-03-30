# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            raise Exception("Empty List")
        if n < 1:
            raise Exception("Invalid n")

        dummy = ListNode(None)
        dummy.next = head

        p1 = dummy
        for _ in range(n):
            if p1 is None:
                raise Exception("n is greater than the length of list.")
            p1 = p1.next

        # get the node
        # p2 = dummy
        # while p1 is not None:
        #     p1 = p1.next
        #     p2 = p2.next
        # return p2

        p2 = dummy
        while p1.next is not None:  # stop at the previous node compared with above
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next  # remove

        return dummy.next
