# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def DFS(self, node):
        if node is None:
            return 0
        l = self.DFS(node.left)
        r = self.DFS(node.right)

        if l + r > self.diameter:
            self.diameter = l + r
        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        diameter = left sub-tree depth + right sub-tree depth
        """
        self.DFS(root)
        return self.diameter
