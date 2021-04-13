# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.DFS(node.left)
        self.DFS(node.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.DFS(root)
        return root
