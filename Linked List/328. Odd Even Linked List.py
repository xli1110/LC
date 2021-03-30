# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Remember to iterate NUM in the while loop!
        """
        if head is None:
            return None

        """
        Auxiliary Arrays - Trash
        O(N) - loop twice
        O(N)
        """
        # # store nodes according to odd/even indices
        # arr_odd = []
        # arr_even = []
        # num = 1
        # p = head
        # while p is not None:
        #     if num & 1 == 1:
        #         arr_odd.append(p)
        #     else:
        #         arr_even.append(p)
        #     num += 1  # note the iteration
        #     p = p.next
        #
        # # construct the new list
        # dummy = ListNode(None)
        # p = dummy
        # for node in arr_odd:
        #     p.next = node
        #     p = node
        # for node in arr_even:
        #     p.next = node
        #     p = node
        #
        # p.next = None  # note the tail processing
        #
        # return dummy.next

        """
        Two Pointers - link odd/even nodes separately, then concatenate them
        O(N) - loop once
        O(1)
        """
        dummy_odd = ListNode(None)
        dummy_even = ListNode(None)
        p1 = dummy_odd
        p2 = dummy_even

        num = 1
        p = head
        while p is not None:
            if num & 1 == 1:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            num += 1
            p = p.next

        p1.next = dummy_even.next  # concatenate odd and even
        p2.next = None  # tail
        return dummy_odd.next
