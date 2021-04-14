# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def DFS(self, node):
        if node is None:
            return
        self.res.append(node)
        self.DFS(node.left)
        self.DFS(node.right)

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            # raise Exception("Empty Tree")
            return None

        self.DFS(root)
        for i in range(len(self.res) - 1):
            self.res[i].left = None
            self.res[i].right = self.res[i + 1]
        self.res[-1].left = None
        self.res[-1].right = None
