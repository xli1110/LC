"""
1 - Traversal
    Preorder, Inorder, Postorder, Levelorder

    Problems:
    94(in)
    144(pre)
    145(post)
    102, 103, 107(level) - see BFS

    Iterative Traversal Code:
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



2 - Recursion
    From top to bottom - Preorder: use variable like self.path, self.res
    From bottom to top - Postorder: L = DFS(node.left), R = DFS(node.right); process L and R; return something
    BST - Inorder: L = DFS(left); process node, use self.pre; R = DFS(right)

    Problems:
    98(valid BST) - inorder with self.pre
    101(symmetric) - DFS(root, root), note if conditions; BFS, note the None node processing
    104(depth) - postorder
    105/106(construct) - Locate i and calculate length from INORDER. See 106 annotation for details.
    110(balance) - postorder
    112/113/437(find path) - self.res.append(self.path[:]) when tar found; self.path.pop() when going up
    114(flatten tree) - auxiliary arr solves the traversal result
    116, 117(link next right node) - DFS(right) BEFORE DFS(left)
    124(max path sum) - postorder; recall 53(max sub-array) and 543(diameter)
    226(invert) - swap
    236(lowest common parent) - postorder
    297(serialization) - arr.pop(0)
    538(BST conversion) - inorder with self.pre_sum
    543(diameter) - postorder
    617(merge) - recall 2(add linked lists) and 106(tree construction)
    Airbnb/Hulu(print N-ary tree) - tree construction/traversal/sort
"""
