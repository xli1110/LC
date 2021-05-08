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
        self.res.append(node.val)
        self.rec(node.left)
        self.rec(node.right)

    def ite(self, root):
        res = []
        stack = []
        node = root
        while node is not None or stack:
            while node is not None:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recursion / Iteration
        O(N)
        O(N)
        """

        """
        Recursion
        """
        # self.rec(root)
        # return self.res

        """
        Iteration
        """
        return self.ite(root)
