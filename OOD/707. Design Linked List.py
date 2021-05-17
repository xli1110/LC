class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    """
    Notes
    0 - dummy node for convenience
    1 - update attributes after operations
        1.1 - self.length += 1, self.length -= 1
        1.2 - IMPORTANT: self.tail = node if node.next is None
    2 - delete/add, p = dummy
        get, p = dummy.next
        p and index ranges are different in each case
        When operating link lists, be very careful about pointer exceeding problems.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = Node(None)  # important dummy node
        self.length = 0
        self.tail = self.dummy  # note this initialization

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            # raise Exception("Invalid Index")
            return -1

        p = self.dummy.next

        for _ in range(index):
            p = p.next

        return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)

        node.next = self.dummy.next
        self.dummy.next = node

        if node.next is None:  # note that the added head may also be the tail
            self.tail = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)

        self.tail.next = node

        self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.length:
            return

        p = self.dummy
        node = Node(val)

        for _ in range(index):
            p = p.next

        node.next = p.next
        p.next = node

        self.length += 1
        if node.next is None:  # may add at tail
            self.tail = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.length - 1:
            # note here we can not delete the (length)th node, because it does not exist
            # different from the addAtIndex
            return

        p = self.dummy

        for _ in range(index):
            p = p.next

        p.next = p.next.next

        self.length -= 1
        if p.next is None:  # may delete the tail node
            self.tail = p


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


if __name__ == "__main__":
    def test_print(l):
        p = l.dummy.next
        while p is not None:
            print(p.val)
            p = p.next


    l = MyLinkedList()

    l.addAtHead(1)
    # test_print(l)

    l.addAtTail(3)
    test_print(l)

    l.addAtIndex(1, 2)
    test_print(l)

    print(l.get(1))
    l.deleteAtIndex(1)
    print(l.get(1))
