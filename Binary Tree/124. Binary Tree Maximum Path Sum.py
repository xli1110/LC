# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_val = None

    def DFS(self, node):
        """
        Recall 53 and 543.

        cur_val - 53
        If L or R is positive, then it CONTRIBUTES to the result, adding it.

        return_val - 543
        max(L + val, R + val, val)
        <=>
        max(L, R) + val if max(L, R) > 0 else val
        """
        if node is None:
            return 0
        L = self.DFS(node.left)
        R = self.DFS(node.right)

        cur_val = node.val
        if L > 0:
            cur_val += L
        if R > 0:
            cur_val += R

        if self.max_val is None or cur_val > self.max_val:
            self.max_val = cur_val

        return max(L, R) + node.val if max(L, R) > 0 else node.val

    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            raise Exception("Empty Tree")

        self.DFS(root)
        return self.max_val
