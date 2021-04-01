# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def rec(self, node):
        if node is None:
            return
        self.rec(node.left)
        self.rec(node.right)
        self.res.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recursion / Iteration
        O(N)
        O(N)
        """

        """
        Recursion
        """
        self.rec(root)
        return self.res

        """
        Iteration
        """
        # TBH IDK
