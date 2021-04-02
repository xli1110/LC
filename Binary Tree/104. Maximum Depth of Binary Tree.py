from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, node):
        """
        O(N)
        O(N) worst; O(logN) average; O(height) exact
        """
        if node is None:
            return 0
        return max(self.DFS(node.left), self.DFS(node.right)) + 1

    def BFS(self, root):
        if root is None:
            return 0
        q = deque()
        q.append(root)
        depth = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            depth += 1
        return depth

    def maxDepth(self, root: TreeNode) -> int:

        # return self.DFS(root)

        return self.BFS(root)
