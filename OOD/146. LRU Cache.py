class Node:
    def __init__(self, key, val):
        self.key = key  # We need this to backtrack the key in the dictionary.
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:
    """
    Hash Map + Doubly Linked List
    """

    def __init__(self, capacity: int):
        """
        cache - dictionary
        cache[key] = Node(val)

        DLL - doubly linked list
        head <-> node <-> node <-> ... <-> tail
        """
        self.cache = {}

        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head

        self.cap = capacity
        self.size = 0

    def get(self, key: int) -> int:
        """
        1 - Key does not exist.
        2 - Find the Key-Node pair in self.cache.
        3 - Remove this node from the list.
        4 - Move it to the first position.
        """
        # 1 - Not Exist
        if key not in self.cache:
            return -1

        # 2 - Find Pair
        node = self.cache[key]
        val = node.val

        # 3/4
        self.remove_node(node)
        self.add_to_first(node)

        return val

    def put(self, key: int, value: int) -> None:
        """
        1 - Add/Update the Key-Node pair in self.cache.
        2 - Remove this node from the list if it exists.
        3 - Add this node to the first position.
        3 - Remove the last node from list AND MAP if size exceeds.
        """
        if key in self.cache:
            # 1 - Update the Pair
            node = self.cache[key]
            node.val = value
            # 2 - Remove from List
            self.remove_node(node)
        else:
            # 1 - Add the Pair
            node = Node(key, value)
            self.cache[key] = node

        # 3 - Add to First
        self.add_to_first(node)

        # 4 - Remove Last
        if self.size > self.cap:
            last = self.tail.pre
            self.remove_node(last)
            # do NOT forget this
            self.cache.pop(last.key)

    def remove_node(self, node):
        """
        Remove the node from the list.
        """
        p1 = node.pre
        p2 = node.next

        p1.next = p2
        p2.pre = p1

        self.size -= 1

    def add_to_first(self, node):
        """
        Add a new node to the first position.
        """
        t = self.head.next

        self.head.next = node
        node.pre = self.head

        node.next = t
        t.pre = node

        self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
