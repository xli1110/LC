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
        """
        cur_dia = L + R

        return = max(L, R) + 1
        """
        if node is None:
            return 0

        L = self.DFS(node.left)
        R = self.DFS(node.right)

        cur_dia = L + R
        if cur_dia > self.diameter:
            self.diameter = cur_dia

        return max(L, R) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        diameter = left sub-tree depth + right sub-tree depth
        """
        self.DFS(root)
        return self.diameter
