# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, n1, n2):
        if n1 is None and n2 is None:
            return None

        v1 = n1.val if n1 is not None else 0
        v2 = n2.val if n2 is not None else 0

        node = TreeNode(v1 + v2)
        node.left = self.DFS(
            n1.left if n1 is not None else None,
            n2.left if n2 is not None else None
        )
        node.right = self.DFS(
            n1.right if n1 is not None else None,
            n2.right if n2 is not None else None
        )

        return node

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return self.DFS(root1, root2)
