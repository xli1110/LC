"""
1 - Traversal
    Preorder, Inorder, Postorder, Levelorder

    Problems:
    94(in)
    144(pre)
    145(post)
    102, 103, 107(level) - see BFS

    Iterative Traversal:
    # init
    res = []
    stack = []
    node = root

    # loop
    while node is not None or stack:

        - Pre (M -> L -> R)
        while node is not None:
            res.append(node.val)  # visit
            stack.append(node.right)  # push R
            node = node.left  # move to L
        node = stack.pop()  # pop

        - In (L -> M -> R)
        while node is not None:
            stack.append(node)  # push M
            node = node.left  # move to L
        node = stack.pop()  # pop
        res.append(node.val)  # visit
        node = node.right  # move to R

        - Post (M -> R -> L, return [::-1])
        while node is not None:
            res.append(node.val)  # visit
            stack.append(node.left)  # push L
            node = node.right  # move to R
        node = stack.pop()  # pop

    # return
    Pre/In return res; Post return res[::-1]

2 - Recursion

    Problems:
    101(symmetric) - DFS(root, root), note if conditions; BFS, note the None node processing
    104, 111(depth)
    105/106(construct) - Locate i and calculate length from INORDER. See 106 annotation for details.
    112(path seeking) - self.res.append(self.path[:]) when tar found; self.path.pop() when going up
    116, 117(link next right node)






DFS
114,430 TBD
"""
