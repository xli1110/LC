# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, h1, h2):
        dummy = ListNode(None)
        p = dummy
        p1 = h1
        p2 = h2

        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p.next = p1
                p = p.next
                p1 = p1.next
            else:
                p.next = p2
                p = p.next
                p2 = p2.next

        p.next = p1 if p2 is None else p2
        return dummy.next

    def m_sort(self, head):
        """
        1 - Find the mid with two pointers.
        2 - Divide the list.
        3 - Recursion.
        """
        if head is None or head.next is None:  # base case
            return head

        # find the mid
        # Case 1: A -> B -> C -> D -> E, slow stops at C
        # Case 2: A -> B -> C -> D -> E -> F, slow stops at C
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # divide the list
        mid = slow.next
        slow.next = None

        # merge two sorted lists
        return self.merge(self.m_sort(head), self.m_sort(mid))

    def naive_sort(self, head):
        arr = []
        p = head
        while p is not None:
            arr.append(p.val)
            p = p.next

        arr.sort()
        p = head
        i = 0
        while p is not None:
            p.val = arr[i]
            p = p.next
            i += 1

        return head

    def sortList(self, head: ListNode) -> ListNode:
        # return self.naive_sort(head)
        return self.m_sort(head)
