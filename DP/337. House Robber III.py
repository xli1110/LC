# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, node):
        """
        return x_0, x_1
        x_0 = the maximal value if we do NOTvisit the current node
        x_1 = the maximal value if we visit the current node
        """
        if node is None:
            return 0, 0

        L0, L1 = self.DFS(node.left)
        R0, R1 = self.DFS(node.right)

        # WRONG
        cur_0 = max(L1, R1)
        cur_1 = max(L0, R0) + node.val

        # RIGHT
        cur_0 = max(L0, L1) + max(R0, R1)
        cur_1 = L0 + R0 + node.val

        return cur_0, cur_1

    def rob(self, root: TreeNode) -> int:
        return max(self.DFS(root))
