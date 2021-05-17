"""
Tips:
    1 - Use dummy for convenience.
        dummy = Node(None)
        p = dummy
        dummy.next = head  # do not forget this
        xxxxxxxxx
        return dummy.next
    2 - Always check whether the node is None before visiting its attributes.
    3 - reverse/concatenate: temp + iterate + operation
        while p2 is not None:
            temp1 = p1
            temp2 = p2
            p1 = temp2
            p2 = temp2.next
            temp1.next = temp2



1 - Classic Linked List Problems

    Problems:
    2(add linked lists) - while l1 or l2; node = ListNode((v1 + v2 + carry) % 10, None); carry = (v1 + v2 + carry) // 10
    21(merge) - dummy, p = dummy, traverse lists, p = l1 if l2 is None else l2
    61(rotate) - calculate k % length; find new head/tail; link tail to head, link new tail to None
    203(remove val) - p1 = dummy, p2 = head; loop: p1.next = p2.next, p2 = p2.next or p1 = p1.next, p2 = p2.next
    206(reserve) - p1 = None, p2 = head
    234(palindrome)
    328(odd even transform) - dummy_odd, p1; dummy_even p2; p1.next = dummy_even.next, p2.next = None



2 - Two Pointers (Fast and Slow)

    Problems:
    19(remove nth from end) - p1 moves n steps from dummy; p1 and p2 move to the end until p1 is None
    141(cycle) - p1 = head, p2 = head.next; while p2 is not None and p2.next is not None
    142(cycle start) - 141 + cycle length + 19
    160(intersection) - p1 moves L1 + C + L2 + C steps and p2 moves L2 + C + L1 steps



3 - Others
    138(copy with random pointer) - loop twice store + link; note d.get(key, None)
    148(sort) - merge sort; return merge(m_sort(head), m_sort(mid))
    Hulu(transform) - find mid; reverse; concatenate. see 328 similar
"""
