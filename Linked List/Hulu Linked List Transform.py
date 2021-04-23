class Node:
    def __init__(self):
        self.val = None
        self.next = None


class Problem1:
    """
    Given a singly linked list.
    1 -> 2 -> 3 -> ... -> N - 1 -> N
    Transform it into the following type.
    1 -> N -> 2 -> N - 1 -> 3 -> N - 2 -> ...

    Requirement
    O(N)
    O(1)

    Discussion:
    I - Naive method, use an array to store nodes and link them together.
    Int - Yes, can you give me a O(1) space complexity method?
    I - It will be easy if I can traverse from the end.
        Can I change the list node structure?
        Say, make it a doubly linked list?
    Int - Yes, but actually, you still need O(N) space.
    I - Ah yes, we need N more pointers.

    Think

    I - I can loop the list twice, and transform it.
        Here, I reach O(1) space but O(N ** 2) time.
    Int - Yes, can we reach O(N) and O(1)?
          How can we traverse from the end?
          Think about the transformed structure, can we DIVIDE it into TWO parts?
    I - Yes!
        We can at first divide the list from the mid and reverse the last part.
        Then, concatenate two parts as requested.
    Int - Perfect, implement it.
    I - In terms of robustness, we need to discuss some corner cases.
    Int - Yes, you can note them in your own style.
    """

    def reverse_list(self, head):
        p1 = None
        p2 = head
        while p2 is not None:
            t = p2
            p2 = p2.next
            t.next = p1
            p1 = t
        return p1

    def find_mid(self, head):
        p1 = head

    def transform(self,head):
        if head is None:
            raise Exception("Empty List")
