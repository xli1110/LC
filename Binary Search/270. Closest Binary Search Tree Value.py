"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root, target):
        if root is None:
            raise Exception("Empty Tree")

        res = root.val
        while root is not None:
            # iterate res
            if abs(root.val - target) < abs(res.val - target):
                res.val = root.val

            # binary search tree
            if root.val == target:
                return root.val
            elif target > root.val:
                root = root.right
            else:
                root = root.left

        return res.val
