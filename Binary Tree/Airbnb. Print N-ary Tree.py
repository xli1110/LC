class Node:
    def __init__(self):
        self.val = ""
        self.children = []


class Problem1:
    """
    TBD: Sort children by their values' lexical order.

    Print N-ary Tree
    Input = [s1, s2, s3, ..., sN]
    Tree nodes in the same level should be printed in the lexical order from top to bottom.

    Example
    input:
    /bin/usr/bash
    /var/test/.ssh
    /var/log/wifi.log
    /opt
    /xyz

    char range:
    `[a-zA-Z0-9./]`

    output:
    /
    +-- bin
    |   +-- usr
    |       +-- bash
    +-- opt
    +-- var
    |   +-- log
    |   |   +-- wifi.log
    |   +-- test
    |       +-- .ssh
    +-- xyz

    the indent should be 4 blanks
    new node starts with `+-- `
    the siblings are linked by '|'
    """

    def m_node(self, s):
        n = Node()
        n.val = s
        return n

    def m_tree(self, root, arr):
        """
        Two Pointers n1 and n2
        Similar to generate N linked lists with the same root.
        """
        n1 = root
        for x in arr:
            values = {child.val: child for child in n1.children}
            if x in values:
                n1 = values[x]  # avoid adding one node twice
            else:
                n2 = Node()
                n2.val = x
                n1.children.append(n2)
                n1 = n2

    def node_sort(self, node):
        """
        Sort a node's children nodes by the lexical order.
        Naive method, temp arr.

        TBH, it sucks as swapping parent nodes' values.
        Then, the parent-children relationship will not hold.

        We need to sort the NODE but not the VALUE!
        """
        arr = [child.val for child in node.children]
        arr.sort()
        for i, x in enumerate(arr):
            node.children[i].val = x

        for child in node.children:
            self.node_sort(child)

    def bubble_sort(self, node):
        """
        Compared with the incorrect sort above, we swap nodes but not their values.
        """
        for i in range(len(node.children)):
            for j in range(i + 1, len(node.children)):
                if node.children[i].val > node.children[j].val:
                    node.children[i], node.children[j] = node.children[j], node.children[i]

        for child in node.children:
            self.bubble_sort(child)

    def partition(self, arr, low, high, pivot):
        i_less = low
        for i in range(low, high):
            if arr[i].val <= pivot:
                arr[i], arr[i_less] = arr[i_less], arr[i]
                i_less += 1
        arr[i_less], arr[high] = arr[high], arr[i_less]
        return i_less

    def q_sort(self, arr, low, high):
        if high - low < 1:
            return
        pivot = arr[-1].val
        mid = self.partition(arr, low, high, pivot)
        self.q_sort(arr, low, mid - 1)
        self.q_sort(arr, mid + 1, high)

    def q_s_invoker(self, node):
        children = node.children
        low = 0
        high = len(children) - 1
        self.q_sort(node.children, low, high)

        for child in node.children:
            self.q_s_invoker(child)

    def DFS_print(self, node, depth):
        if depth == 0:
            print("/")
        elif depth == 1:
            print("+-- " + node.val)
        else:
            print("|" + "    " * (depth - 1) + "+-- " + node.val)

        for child in node.children:
            self.DFS_print(child, depth + 1)


if __name__ == "__main__":
    s_list = [
        "/bin/usr/bash",
        "/var/test/spark.ssh",
        "/var/log/wifi.log",
        "/opt",
        "/xyz"
    ]
    p1 = Problem1()

    # make the root
    root = Node()
    root.val = "/"

    # make the tree
    for s in s_list:
        p1.m_tree(root, s.split("/")[1:])

    # sort
    # p1.node_sort(root)
    # p1.bubble_sort(root)
    p1.q_s_invoker(root)

    # print
    p1.DFS_print(root, 0)
