"""
1 - Traversal

    When designing iterative functions, take the tree below as an example.
        A

    B       C


    Iterative Traversal Model:
    # init
    res = []
    stack = []
    node = root

    # loop
    while node is not None or stack:

        - Pre (M -> L -> R)
        while node is not None:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right

        - In (L -> M -> R)
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right

        - Post (M -> R -> L, return [::-1])
        while node is not None:
            res.append(node.val)
            stack.append(node)
            node = node.right
        node = stack.pop()
        node = node.left

    # return
    Pre/In return res; Post return res[::-1]

    Problems:
    94(in)
    144(pre)
    145(post)
    102, 103, 107(level) - see BFS


2 - Recursion
    <Preorder>
    From top to bottom: process node with variables like self.path, self.res; DFS(L), DFS(R).
    <Postorder>
    From bottom to top: L = DFS(node.left), R = DFS(node.right); process L and R; return something.
    <Inorder>
    BST: L = DFS(left); process node with self.pre and L; R = DFS(right); may return something.

    Problems:
    <Preorder>
    112/113/437(find path) - self.res.append(self.path[:]) when tar found; self.path.pop() when going up. See 113.
    114(flatten tree) - modify M -> L -> R to R -> L -> M, and link the list from end to start
    116, 117(link next right node) - find node_next for node's children(linked list); call DFS(right) BEFORE DFS(left)
    226(invert) - swap

    <Postorder>
    101(symmetric) - DFS(root, root), note if conditions; BFS, note the None node processing
    104(depth)
    105/106(construct) - Locate i and calculate length from INORDER. See 106 annotation for details.
    110(balance)
    124(max path sum) - recall 53(max sub-array) and 543(diameter)
    236(lowest common parent) - L is None and R is None; L is not None and R is not None; return the one not None
    543(diameter) - cur_val = L + R; return_val = max(L, R) + 1
    617(merge) - recall 2(add linked lists) and 106(tree construction)

    <Inorder>
    98(valid BST) - self.pre
    <TBD>450(delete node in BST)
    538(BST conversion) - self.pre_sum



3 - Others:
    297(serialization)
    Airbnb/Hulu(print N-ary tree) - tree construction/traversal/sort
"""
