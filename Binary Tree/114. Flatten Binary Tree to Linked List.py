# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []
        self.next_node = None

    def DFS(self, node):
        if node is None:
            return
        self.res.append(node)
        self.DFS(node.left)
        self.DFS(node.right)

    def DFS2(self, node):
        """
        Modify M -> L -> R to R -> L -> M, and link the list from end to start.

        Can not link from start to end, which destroys tree structure.

        Example of preorder traversal:
        For each node, we have

        self.pre.right = node
        node.left = None

        then, we can not visit node.left since it was set to None.
        """
        if node is None:
            return

        self.flatten(node.right)
        self.flatten(node.left)

        node.right = self.next_node
        node.left = None
        self.next_node = node

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            # raise Exception("Empty Tree")
            return None

        """
        Auxiliary Array
        O(N)
        O(N)
        """
        # self.DFS(root)
        # for i in range(len(self.res) - 1):
        #     self.res[i].left = None
        #     self.res[i].right = self.res[i + 1]
        # self.res[-1].left = None
        # self.res[-1].right = None

        """
        In-Place Swap
        O(N)
        O(1)
        """
        self.DFS2(root)
