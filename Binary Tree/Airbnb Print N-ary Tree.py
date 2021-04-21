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
    "/*
    input:

    /bin/usr/bash
    /var/test/.ssh
    /var/log/wifi.log
    /opt
    /xyz

    char range: `[a-zA-Z0-9./]`

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

    * the indent should be 4 blanks
    * new node starts with `+-- `
    * the siblings are linked by '|'
    */
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
        "/var/test/.ssh",
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

    p1.DFS_print(root, 0)
