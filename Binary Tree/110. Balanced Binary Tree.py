# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, node):
        if node is None:
            return 0

        l = self.DFS(node.left)
        r = self.DFS(node.right)

        if l < 0 or r < 0:
            return -1

        if abs(l - r) <= 1:
            return max(l, r) + 1
        else:
            return -1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.DFS(root) >= 0
