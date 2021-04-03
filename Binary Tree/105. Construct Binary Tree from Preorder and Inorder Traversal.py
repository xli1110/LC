# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, inorder, preorder, in_low, in_high, pre_low, pre_high):
        if in_low > in_high or pre_low > pre_high:
            return None

        val = preorder[pre_low]
        i = inorder.index(val)

        node = TreeNode(val)

        node.left = self.DFS(
            inorder,
            preorder,
            in_low,
            i - 1,
            pre_low + 1,
            pre_low + 1 + ((i - 1) - in_low)
        )
        node.right = self.DFS(
            inorder,
            preorder,
            i + 1,
            in_high,
            pre_high - (in_high - (i + 1)),
            pre_high
        )
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            raise Exception("Empty Tree")
        if len(preorder) != len(inorder):
            raise Exception("Invalid Traversal")

        return self.DFS(inorder, preorder, 0, len(inorder) - 1, 0, len(preorder) - 1)
