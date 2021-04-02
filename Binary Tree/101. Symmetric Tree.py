from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def BFS(self, root):
        """
        Typically, we do not enqueue empty nodes in BFS as shown below.
        However, if so, we will suck in this problem.
        Assuming a certain level is [None, None, 1, 2, 2, None, None, 1], it is definitely unsymmetrical.
        But if we do not enqueue None nodes after leaves, this level will look like [1, 2, 2, 1],
        which ridiculously implies that the symmetry holds.
        """
        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node is not None:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)

            if level != level[::-1]:
                return False
        return True

    def DFS(self, p, q):
        """
        Remember the first three if conditions.
        Useful.
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return self.DFS(p.left, q.right) and self.DFS(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            raise Exception("Empty Tree")

        # return self.DFS(root, root)

        return self.BFS(root)
