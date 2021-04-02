# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, inorder, postorder, in_low, in_high, post_low, post_high):
        """
        inorder = [L, node(index = i), R]
        postorder = [L, R, node]

        i = inorder.index(postorder[post_high])
        Let x denotes the pointer passed by DFS, and x' denotes the updated pointers we feed to recursive function.

        We can simply divide inorder into L and R as below.
        L(inorder):
        in_low' = in_low
        in_high' = i - 1

        R(inorder):
        in_low' = i + 1
        in_high' = in_high


        Then, we divide postorder based on the LENGTH of L and R.
        L(postorder): low is fixed, calculate high based on the LENGTH
        post_low' = post_low
        post_high' - post_low' = in_high' - in_low'    =>    post_high' = post_low + ((i - 1) - in_low)

        R(postorder): high is fixed, calculate low based on the LENGTH
        post_high' - post_low' = in_high' - in_low'    =>    post_low' = (post_high - 1) - (in_high - (i + 1))
        post_high' = post_high - 1
        """
        if in_low > in_high or post_low > post_high:
            return None

        val = postorder[post_high]
        i = inorder.index(val)

        # construct
        node = TreeNode(val)  # node

        # WRONG, low and high VARY during the recursion!
        # node.left = self.DFS(inorder, postorder, 0, i - 1, 0, i - 1)
        # node.right = self.DFS(inorder, postorder, i + 1, len(inorder) - 1, i, len(postorder) - 2)

        node.left = self.DFS(
            inorder, postorder,
            in_low,
            i - 1,
            post_low,
            post_low + (i - 1 - in_low)
        )  # left
        node.right = self.DFS(
            inorder, postorder,
            i + 1,
            in_high,
            post_high - 1 - (in_high - (i + 1)),
            post_high - 1
        )  # right

        return node  # Return each sub-root. When backtracking to the root, return it to the invoker.

    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        if not inorder or not postorder:
            raise Exception("Empty Tree")
        if len(inorder) != len(postorder):
            raise Exception("Invalid Traversal")

        return self.DFS(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)
