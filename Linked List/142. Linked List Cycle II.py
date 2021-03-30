# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        # 1 - check cycle
        p1 = head
        p2 = head.next
        has_cycle = False
        while p2 is not None and p2.next is not None:
            if p1 == p2:
                has_cycle = True
                break
            p1 = p1.next
            p2 = p2.next.next

        if not has_cycle:
            return None

        # 2 - cycle length
        cycle_length = 1
        p2 = p1.next
        while p1 != p2:
            p2 = p2.next
            cycle_length += 1

        # 3 - problem 19, the nth node from the end
        # L = cycle + non
        # p1 moves cycle
        # p1 and p2 moves non, meeting at the start
        dummy = ListNode(None)
        dummy.next = head
        p1 = dummy
        for _ in range(cycle_length):
            p1 = p1.next

        p2 = dummy
        while p2 != p1:
            p1 = p1.next
            p2 = p2.next

        return p1


if __name__ == "__main__":
    head = ListNode(1)
    p = head

    node = ListNode(2)
    p.next = node
    p = p.next

    node = ListNode(3)
    p.next = node
    p = p.next

    node = ListNode(4)
    p.next = node
    p = p.next
    start = node

    node = ListNode(5)
    p.next = node
    p = p.next

    node = ListNode(6)
    p.next = node
    p = p.next

    node = ListNode(7)
    p.next = node
    p = p.next
    p.next = start

    sol = Solution()
    print(sol.detectCycle(head).val)
