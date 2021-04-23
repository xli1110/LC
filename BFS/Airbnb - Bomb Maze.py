from collections import deque


class Problem1:
    """
    2D Matrix Path with Restrictions

    Given a 2D (X * Y) matrix with N bombs located at (xi, yi)， where 0 < X, Y, N <= 1000.
    start = [0][0]
    end = [X - 1][Y - 1]
    Find the shortest path from start to end which has the maximum d_shortest,
    where d_shortest denotes the shortest Manhattan distance between the bomb and the path.

    Example:
    N = 2
    Location: (1, 2), (2, 3).
    output: 9(shortest path length), 2(shortest distance)

           0     1     2     3     4     5
        +-----+-----+-----+-----+-----+-----+
        |     |     |     |     |     |     |
    0   |start|     |     |     |     |     |
        |  |  |     |     |     |     |     |
        +--+--+-----+-----+-----+-----+-----+
        |  |  |     | xxx |     |     |     |
    1   |  v  |     |xxxxx|     |     |     |
        |  |  |     | xxx |     |     |     |
        +--+--+-----+-----+-----+-----+-----+
        |  |  |     |     | xxx |     |     |
    2   |  v--+-->  |     |xxxxx|     |     |
        |     |  |  |     | xxx |     |     |
        +-----+--+--+-----+-----+-----+-----+
        |     |  |  |     |     |     |     |
    3   |     |  v--+-->  |     |     |     |
        |     |     |  |  |     |     |     |
        +-----+-----+--+--+-----+-----+-----+
        |     |     |  |  |     |     |     |
    4   |     |     |  v--+--> -+--> -+>end |
        |     |     |     |     |     |     |
        +-----+-----+-----+-----+-----+-----+

    I - BFS, find all paths and calculate the shortest distance.
    Int - Let 0 < X, Y, N, <= 1000. Is your algorithm acceptable?
    I - (X * Y) ** 2.
    Int - Sure?
    I - Wrong, should be exponential complexity, like 4 ** (X + Y).
    Int - Yes, how to optimize it?

    Think.

    I - No ideas, any remind?
    Int - How to calculate one point's shortest distance to the bombs?
    I - Generate one matrix for one bomb, denoting this distance, O(XYN). s1, get mat[][].
        When traversing, at each point, we check N matrices and find the shortest distance, O(N). s2
    Int - Can we only use ONE auxiliary matrix?
    I - Yes, we traverse all bombs and update the distance matrix if we find a smaller value at s1.
        Then s2's complexity will be O(1).

    Think.
    I - Reminds please.
    Int - What if we know 2 is the shortest distance, and let you find the path?
    I - We traverse mat and block points whose value < 2.
    Int - Right, so what if we do not know 2?
    I - We can try from the maximal distance to 0, if we find the path, then we break and return.
    Int Right, complexity?
    I - O(XY * (X + Y)), cubic complexity.
    Int - Right, try to implement your ideas.
    """

    def check_exceed(self, x, y, X, Y):
        return 0 <= x < X and 0 <= y < Y

    """
    Functions for matrix generation.
    """

    def BFS_dist(self, x, y, X, Y, mat, searched):
        """
        O(XY)
        (x, y) - bomb location
        mat - shortest distance matrix
        mat[i][j] = shortest distance from (i, j) to the bomb (x, y)
        """
        # init
        dist = 0
        q = deque()
        q.append([x, y])

        # search
        while q:
            # level order traversal
            for _ in range(len(q)):
                point = q.popleft()
                i = point[0]
                j = point[1]

                if not self.check_exceed(i, j, X, Y):
                    continue
                if searched[i][j]:
                    continue

                searched[i][j] = True
                mat[i][j] = min(dist, mat[i][j])

                # search 4 directions
                q.append([i - 1, j])
                q.append([i + 1, j])
                q.append([i, j - 1])
                q.append([i, j + 1])

            dist += 1  # update
        return mat

    def generate_mat(self, bombs, X, Y):
        """
        O(NXY)
        Loop all bombs.
        """
        # init
        mat = [[9999] * Y for _ in range(X)]

        # loop
        for bomb in bombs:
            searched = [[False] * Y for _ in range(X)]
            self.BFS_dist(bomb[0], bomb[1], X, Y, mat, searched)

        return mat

    """
    Functions for distinct distances set generation.
    """

    def dist_set(self, mat, X, Y):
        """
        O(XY) + O((X + Y)log(X + Y))
        Generate the set of shortest distances.
        """
        # find distinct distances O(XY)
        s = set()
        for i in range(X):
            for j in range(Y):
                if mat[i][j] not in s:
                    s.add(mat[i][j])

        # sort the list O((X + Y)log(X + Y))
        # the largest element this set should be (X + Y)
        arr = list(s)
        arr.sort()
        return arr

    """
    Functions for path seeking.
    """

    def BFS_path(self, x, y, X, Y, mat, searched, min_dist_to_bomb):
        """
        O(XY)
        Search the path from start to end with the min_dist to bombs.
        """
        # init
        path_length = 0
        q = deque()
        q.append([x, y])

        # search
        while q:
            # level order traversal
            for _ in range(len(q)):
                point = q.popleft()
                i = point[0]
                j = point[1]

                if not self.check_exceed(i, j, X, Y):
                    continue
                if searched[i][j]:
                    continue
                if mat[i - 1][j] < min_dist_to_bomb:
                    continue
                # reach the end
                if i == X - 1 and j == Y - 1:
                    return path_length

                searched[i][j] = True

                # search 4 directions
                q.append([i - 1, j])
                q.append([i + 1, j])
                q.append([i, j - 1])
                q.append([i, j + 1])

            path_length += 1  # update

        return None  # no such path found

    def find_path(self, mat, X, Y, dist_list):
        """
        Loop the distinct distance list and find the answer.
        O((X + Y) * XY)
        """
        i = len(dist_list) - 1

        while i >= 0:
            min_dist_to_bomb = dist_list[i]

            if mat[0][0] < min_dist_to_bomb:
                # example
                # min_dist_to_bomb = 5, mat[0][0] = 3
                # we can not find a path starting at [0][0] with minimal distance to the bomb >= 5
                i -= 1
                continue

            searched = [[False] * Y for _ in range(X)]
            path_length = self.BFS_path(0, 0, X, Y, mat, searched, min_dist_to_bomb)
            if path_length is None:
                i -= 1
            else:
                return path_length, min_dist_to_bomb

        return None, None  # no such path exists


if __name__ == "__main__":
    """
    O((X + Y + N) * XY)
    """
    X = 5
    Y = 6
    bombs = [[1, 2], [2, 3]]

    p1 = Problem1()

    # step 1: compute the distance matrix, O(XYN)
    mat = p1.generate_mat(bombs, X, Y)
    print(mat)

    # step 2: compute the distinct distances list, O(XY)
    dist_list = p1.dist_set(mat, X, Y)
    print(dist_list)

    # step 3: path seeking, O((X + Y) * XY)
    path_length, min_dist = p1.find_path(mat, X, Y, dist_list)
    print(path_length, min_dist)
