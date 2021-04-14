# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = None

    def DFS(self, node):
        if node is None:
            return True

        L = self.DFS(node.left)
        if self.pre is not None and self.pre.val >= node.val:
            return False
        self.pre = node
        R = self.DFS(node.right)
        return L and R

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            raise Exception("Empty Tree")

        return self.DFS(root)
