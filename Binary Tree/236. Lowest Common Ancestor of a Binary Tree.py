# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.has_found = False
        self.path = []
        self.res = []

    def DFS(self, node, tar):
        if node is None:
            return
        if self.has_found:
            return

        self.path.append(node)

        if node == tar:
            self.has_found = True
            self.res.append(self.path[:])
            return

        self.DFS(node.left, tar)
        self.DFS(node.right, tar)

        self.path.pop()

    def DFS2(self, node, p, q):
        # base case
        if node is None:  # 1 - reach leaf
            return None
        if node == p or node == q:  # 2 - reach target
            return node

        l = self.DFS2(node.left, p, q)
        r = self.DFS2(node.right, p, q)

        if l is None and r is None:
            # case 1 - Nothing Found
            # p and q are not in sub-trees of node.
            return None

        if l is not None and r is not None:
            # case 2 - Lowest Common Parent Found
            # p and q are in two sub-trees respectively, and the node is the lowest common parent.
            # l == p and r == q
            # or
            # l == q and r == p
            return node

        # case 3 - Higher Common Parent Found
        # p and q are in one sub-tree of node, and the node is a higher common parent.
        # Note here l or r always represents the lowest common parent,
        # since we return the lowest common parent at case 2 and l = self.DFS() passing the value to it.
        return l if r is None else r

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p is None or q is None:
            raise Exception("Target is None")

        """
        Naive
        O(N) - invoke DFS twice, loop once
        O(N)
        """
        # # search path
        # self.path = []
        # self.has_found = False
        # self.DFS(root, p)
        # if not self.has_found:
        #     raise Exception("Node {} has not been found in the given tree.".format(p.val))
        #
        # self.path = []
        # self.has_found = False
        # self.DFS(root, q)
        # if not self.has_found:
        #     raise Exception("Node {} has not been found in the given tree.".format(p.val))
        #
        # # compare two paths
        # path_p = self.res[0]
        # path_q = self.res[1]
        #
        # i = 1  # We have path_p[0] == path_q[0] == root. Thus, we can traverse from 1.
        # j = 1
        # while i <= len(path_p) - 1 and j <= len(path_q) - 1:
        #     if path_p[i] != path_q[j]:
        #         return self.res[0][i - 1]
        #     i += 1
        #     j += 1
        # return path_p[-1] if i == len(path_p) else path_q[-1]  # note condition i == len(path_p)

        """
        Recursion Once
        """
        return self.DFS2(root, p, q)
