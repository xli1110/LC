"""
1 - BFS on Trees

    Problems:
    101(symmetric) - see Binary Tree
    102, 103, 107(level)
    104, 111(depth) - see Binary Tree

    BFS Code:
    from collections import deque

    if root is None:
        raise Exception("xxx")

    # initialization
    res = []
    q = deque()
    q.append(root)

    # BFS
    while q:

        # level loop
        level = []
        for _ in range(len(q)):

            # dequeue the current node
            node = q.popleft()
            level.append(node.val)

            # loop children
            # add new nodes - note the condition may vary
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

        res.append(level)

    return res



2 - BFS on Matrices
    Need a matrix to store searched elements, like searched = [[False] * N for _ in range(M)].
    Otherwise, BFS may stuck in infinite loops.

    Problems:
    200(2D Array)
"""
