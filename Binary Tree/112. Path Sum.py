# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.has_found = False
        self.res = []
        self.path = []

    def DFS(self, node, tar):
        """
        Note the SLICE of self.path.
        Otherwise, self.res is appended by a reference.
        When the DFS return to previous invokes, self.path will be changed, and the values in self.res will also be changed.
        """
        # base case
        if node is None:
            return
        if self.has_found:  # if we need to find ALL paths, remove this
            return

        # operating current node
        self.path.append(node.val)
        tar -= node.val  # do not forget this

        if tar == 0 and node.left is None and node.right is None:  # require a LEAF node at the end
            self.has_found = True
            self.res.append(self.path[:])
            return

        # GOING DOWN. Recursively process current node's children, until reaching leaf nodes.
        self.DFS(node.left, tar)
        self.DFS(node.right, tar)

        # GOING UP. Return to the root, popping out the current node from self.path.
        self.path.pop()

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            raise Exception("Empty Tree")
        self.DFS(root, targetSum)
        return self.has_found
