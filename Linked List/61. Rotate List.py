# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        0 - calculate length, initialize length = -1!!!
        1 - rotate k steps <==> the kth node from the end will be the new head
        2 - link the old tail to the old head
            link the the (k - 1)th node from the end to None as the new tail
        """
        if head is None:
            return None
        if k < 0:
            raise Exception("Invalid k")

        # calculate length
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        length = -1  # note the initialization
        while p is not None:
            length += 1
            p = p.next

        # calculate the real rotation steps (k % length)
        k %= length

        # find the new tail/head
        p = dummy
        for _ in range(k):
            p = p.next
        new_tail = dummy
        while p.next is not None:  # note p.next as we want the tail
            new_tail = new_tail.next
            p = p.next
        if new_tail.next is None:  # no rotation, k == 0
            return head
        new_head = new_tail.next

        # link the new list
        new_tail.next = None
        p = new_head
        while p.next is not None:
            p = p.next
        p.next = head

        return new_head
