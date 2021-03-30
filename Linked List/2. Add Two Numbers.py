# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            raise Exception("At least one list is empty.")

        dummy = ListNode(None)
        p = dummy
        carry = 0

        while l1 is not None or l2 is not None:
            # note None case
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0

            node = ListNode((v1 + v2 + carry) % 10, None)  # %
            carry = (v1 + v2 + carry) // 10  # //

            p.next = node
            p = p.next

            # note iteration
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry != 0:
            p.next = ListNode(carry, None)

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l2 = ListNode(8)
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
