"""
1 - BFS on Trees

    Problems:
    101
    102
    103
    107
    111

    Model:
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

2 - BFS on Graphs or Matrices - the shortest path

Need a matrix to store searched elements.
Otherwise, BFS may stuck in infinite loops.

searched = [[False] * N for _ in range(M)]
"""
