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

        self.DFS(node.left, tar)
        self.DFS(node.right, tar)

        self.path.pop()

    def DFS2(self, node, p, q):
        # base case
        if node is None:  # 1 - reach leaf
            return None
        if node == p or node == q:  # 2 - reach target
            return node

        L = self.DFS2(node.left, p, q)
        R = self.DFS2(node.right, p, q)

        if L is None and R is None:
            # case 1 - Nothing Found
            # p and q are not in sub-trees of node.
            return None

        if L is not None and R is not None:
            # case 2 - Lowest Common Parent Found
            # p and q are in two sub-trees respectively, and the node is the lowest common parent.
            # L == p and R == q
            # or
            # L == q and R == p
            return node

        # case 3 - Higher Common Parent Found
        # p and q are in one sub-tree of node, and the node is a higher common parent.
        #
        # Example:
        # Assume node has L and R, and L is the lowest common parent.
        # L is the lowest common parent
        # => p and q are in L, node's left sub-tree
        # => R must be None, since we can only find ONE p and ONE q from the tree.
        # => We return L to node's parent.
        # => We recursively return L to the root.
        return L if R is None else R

    def naive_method(self, root, p, q):
        # search path for p and q
        self.path = []
        self.has_found = False
        self.DFS(root, p)
        if not self.has_found:
            raise Exception("Node {} has not been found in the given tree.".format(p.val))

        self.path = []
        self.has_found = False
        self.DFS(root, q)
        if not self.has_found:
            raise Exception("Node {} has not been found in the given tree.".format(p.val))

        # compare two paths and find the intersection
        path_p = self.res[0]
        path_q = self.res[1]

        i = 1  # We have path_p[0] == path_q[0] == root. Thus, we can traverse from 1.
        j = 1
        while i <= len(path_p) - 1 and j <= len(path_q) - 1:
            if path_p[i] != path_q[j]:
                return self.res[0][i - 1]
            i += 1
            j += 1

        return path_p[-1] if i == len(path_p) else path_q[-1]  # note condition i == len(path_p)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p is None or q is None:
            raise Exception("Target is None")

        """
        Naive
        O(N) - invoke DFS twice, loop once
        O(N)
        """
        # return self.naive_method(root, p, q)

        """
        Recursion Once
        """
        return self.DFS2(root, p, q)
