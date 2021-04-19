# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.num = 0

    def DFS(self, node, tar):
        if node is None:
            return

        if tar == node.val:
            self.num += 1

        self.DFS(node.left, tar - node.val)
        self.DFS(node.right, tar - node.val)

    def traversal(self, node, tar):
        if node is None:
            return

        self.DFS(node, tar)
        self.traversal(node.left, tar)
        self.traversal(node.right, tar)

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.traversal(root, targetSum)
        return self.num
