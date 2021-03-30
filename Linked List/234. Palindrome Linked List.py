# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        """
        Auxiliary Array
        O(N) - loop twice (slice)
        O(N)
        """
        arr = []
        p = head
        while p is not None:
            arr.append(p.val)
            p = p.next
        return arr == arr[::-1]  # can be optimized with two pointers
