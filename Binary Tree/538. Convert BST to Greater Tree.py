# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre_sum = 0

    def DFS(self, node):
        if node is None:
            return

        self.DFS(node.right)
        self.pre_sum += node.val
        node.val = self.pre_sum
        self.DFS(node.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.DFS(root)
        return root
