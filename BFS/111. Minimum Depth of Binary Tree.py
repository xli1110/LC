from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def BFS(self, root):
        q = deque()
        q.append(root)
        depth = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return depth
                else:
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
            depth += 1

        raise Exception("Wrong")

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.BFS(root)
