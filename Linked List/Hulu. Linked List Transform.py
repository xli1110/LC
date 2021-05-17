class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Problem:
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
            temp1 = p1
            temp2 = p2
            p1 = temp2
            p2 = p2.next
            temp2.next = temp1
        return p1

    def find_mid(self, head):
        p1 = head
        p2 = head.next
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        return p1

    def transform(self, head):
        if head is None:
            raise Exception("Empty List")
        if head.next is None:
            return head

        # find mid
        temp = self.find_mid(head)
        mid = temp.next
        temp.next = None

        # reverse the second half
        mid = self.reverse_list(mid)

        # concatenate
        # use two pointers for iteration
        p1 = head
        p2 = mid
        while p2 is not None:
            # temp
            temp1 = p1
            temp2 = p2
            # iterate
            p1 = temp2
            p2 = temp1.next
            # link
            temp1.next = temp2

        return head


def make_list(arr):
    dummy = Node(None)
    p = dummy
    for x in arr:
        n = Node(x)
        p.next = n
        p = p.next
    return dummy.next


def print_list(head):
    p = head
    while p is not None:
        print(p.val)
        p = p.next


if __name__ == "__main__":
    # arr = [1, 2, 3, 4, 5]
    arr = [1, 2, 3, 4, 5, 6]
    head = make_list(arr)

    problem1 = Problem()
    print_list(problem1.transform(head))
