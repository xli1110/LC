"""
Tips:
    1 - dummy = Node(None)
        dummy.next = head  # do not forget this
    2 - always check whether the node is None before visiting its attributes



1 - Linked List Design

    Problems:
    707(ADT)



2 - Classic Linked List Problems

    Problems:
    2(add linked lists) - while l1 or l2; node = ListNode((v1 + v2 + carry) % 10, None); carry = (v1 + v2 + carry) // 10
    21(merge) - dummy, p = dummy, traverse lists, p = l1 if l2 is None else l2
    61(rotate) - calculate k % length; find new head/tail; link tail to head, link new tail to None
    203(remove val) - p1 = dummy, p2 = head; loop: p1.next = p2.next, p2 = p2.next or p1 = p1.next, p2 = p2.next
    206(reserve) - p1 = None, p2 = head; loop: t = p2
    234(palindrome)
    328(odd/even) - dummy_odd, p1; dummy_even p2; p1.next = dummy_even.next, p2.next = None



3 - Two Pointers (Fast and Slow)

    Problems:
    19(remove nth from end) - p1 moves n steps from dummy; p1 and p2 move to the end until p1 is None
    141(cycle) - p1 = head, p2 = head.next; while p2 is not None and p2.next is not None
    142(cycle start) - 141 + cycle length + 19
    160(intersection) - p1 moves L1 + C + L2 + C steps and p2 moves L2 + C + L1 steps



4 - Others
    138(copy with random pointer) - loop twice as storing nodes and linking them; note d.get(key, None)
"""
