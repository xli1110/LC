"""
1 - BFS on Trees

    Problems:
    101(symmetric) - see Binary Tree
    102, 103, 107(level)
    104, 111(depth) - see Binary Tree

    Model:
    # initialization
    res = []
    q = deque()
    q.append(root)

    # BFS
    while q:
        # level order loop
        level = []
        for _ in range(len(q)):

            # dequeue the current node
            node = q.popleft()
            level.append(node.val)

            # loop children
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
    200(2D array) - 2D array BFS
    Airbnb(bomb maze) - 2D array level order BFS

    Model:
    def check_exceed(x, y, X, Y):
        return 0 <= x < X and 0 <= y < Y

    # init
    path_length = 0
    q = deque()
    q.append([x_start, y_start])

    # search
    while q:
        # level order traversal
        for _ in range(len(q)):
            point = q.popleft()
            i = point[0]
            j = point[1]

            # check termination conditions for a point
            # c1 - exceed
            # c2 - searched
            # ci - other conditions from the problem

            if not self.check_exceed(i, j, X, Y):
                continue
            if searched[i][j]:
                continue
            if mat[i - 1][j] < min_dist_to_bomb:
                continue
            if i == x_end and j == y_end:  # reach the end
                return path_length

            # process the current point
            searched[i][j] = True

            # search 4 directions
            q.append([i - 1, j])
            q.append([i + 1, j])
            q.append([i, j - 1])
            q.append([i, j + 1])

        path_length += 1  # update

    return None  # no such path found
"""
